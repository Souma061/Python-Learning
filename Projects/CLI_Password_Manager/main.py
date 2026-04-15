import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

from manager import delete_entry, get_entry, list_entries, load_data, save_data, set_entry


class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("760x520")
        self.root.minsize(700, 460)

        self.master_password = None
        self.data = {}

        self.search_var = tk.StringVar()
        self.service_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.show_password_var = tk.BooleanVar(value=False)
        self.status_var = tk.StringVar(value="Unlock an existing vault or create a new one.")

        self._build_unlock_frame()
        self._build_main_frame()
        self._show_unlock_screen()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def _build_unlock_frame(self):
        self.unlock_frame = ttk.Frame(self.root, padding=24)
        self.unlock_frame.columnconfigure(0, weight=1)

        ttk.Label(
            self.unlock_frame,
            text="Password Manager",
            font=("TkDefaultFont", 18, "bold"),
        ).grid(row=0, column=0, pady=(0, 10))

        ttk.Label(
            self.unlock_frame,
            text="Enter your master password to unlock the vault.",
        ).grid(row=1, column=0, pady=(0, 16))

        password_row = ttk.Frame(self.unlock_frame)
        password_row.grid(row=2, column=0, sticky="ew")
        password_row.columnconfigure(1, weight=1)

        ttk.Label(password_row, text="Master Password").grid(row=0, column=0, padx=(0, 10))
        self.unlock_password_entry = ttk.Entry(password_row, show="*")
        self.unlock_password_entry.grid(row=0, column=1, sticky="ew")
        self.unlock_password_entry.bind("<Return>", lambda event: self.unlock_vault())

        buttons = ttk.Frame(self.unlock_frame)
        buttons.grid(row=3, column=0, pady=18)

        ttk.Button(buttons, text="Unlock Vault", command=self.unlock_vault).grid(
            row=0, column=0, padx=6
        )
        ttk.Button(buttons, text="Create New Vault", command=self.create_new_vault).grid(
            row=0, column=1, padx=6
        )

    def _build_main_frame(self):
        self.main_frame = ttk.Frame(self.root, padding=16)
        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=2)
        self.main_frame.rowconfigure(1, weight=1)

        header = ttk.Frame(self.main_frame)
        header.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 12))
        header.columnconfigure(1, weight=1)

        ttk.Label(header, text="Search").grid(row=0, column=0, padx=(0, 8))
        search_entry = ttk.Entry(header, textvariable=self.search_var)
        search_entry.grid(row=0, column=1, sticky="ew")
        search_entry.bind("<KeyRelease>", lambda event: self.refresh_entries())

        ttk.Button(header, text="Save Vault", command=self.save_vault).grid(
            row=0, column=2, padx=(8, 0)
        )
        ttk.Button(header, text="Change Master Password", command=self.change_master_password).grid(
            row=0, column=3, padx=(8, 0)
        )

        list_frame = ttk.LabelFrame(self.main_frame, text="Stored Entries", padding=10)
        list_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        self.entry_tree = ttk.Treeview(
            list_frame,
            columns=("service", "username"),
            show="headings",
            height=14,
        )
        self.entry_tree.heading("service", text="Service")
        self.entry_tree.heading("username", text="Username")
        self.entry_tree.column("service", width=180, anchor="w")
        self.entry_tree.column("username", width=180, anchor="w")
        self.entry_tree.grid(row=0, column=0, sticky="nsew")
        self.entry_tree.bind("<<TreeviewSelect>>", self.on_entry_selected)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.entry_tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.entry_tree.configure(yscrollcommand=scrollbar.set)

        form_frame = ttk.LabelFrame(self.main_frame, text="Entry Details", padding=12)
        form_frame.grid(row=1, column=1, sticky="nsew")
        form_frame.columnconfigure(1, weight=1)

        ttk.Label(form_frame, text="Service").grid(row=0, column=0, sticky="w", pady=5)
        ttk.Entry(form_frame, textvariable=self.service_var).grid(
            row=0, column=1, sticky="ew", pady=5
        )

        ttk.Label(form_frame, text="Username").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Entry(form_frame, textvariable=self.username_var).grid(
            row=1, column=1, sticky="ew", pady=5
        )

        ttk.Label(form_frame, text="Password").grid(row=2, column=0, sticky="w", pady=5)
        self.password_entry = ttk.Entry(form_frame, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=2, column=1, sticky="ew", pady=5)

        ttk.Checkbutton(
            form_frame,
            text="Show password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
        ).grid(row=3, column=1, sticky="w", pady=(0, 10))

        actions = ttk.Frame(form_frame)
        actions.grid(row=4, column=0, columnspan=2, pady=(4, 0))

        ttk.Button(actions, text="Add / Update", command=self.save_entry).grid(
            row=0, column=0, padx=5
        )
        ttk.Button(actions, text="Delete", command=self.remove_entry).grid(row=0, column=1, padx=5)
        ttk.Button(actions, text="Clear", command=self.clear_form).grid(row=0, column=2, padx=5)

        ttk.Label(
            self.main_frame,
            textvariable=self.status_var,
            foreground="steel blue",
        ).grid(row=2, column=0, columnspan=2, sticky="w", pady=(12, 0))

    def _show_unlock_screen(self):
        self.main_frame.grid_forget()
        self.unlock_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.unlock_password_entry.focus_set()

    def _show_main_screen(self):
        self.unlock_frame.place_forget()
        self.main_frame.pack(fill="both", expand=True)
        self.refresh_entries()
        self.clear_form()

    def unlock_vault(self):
        master_password = self.unlock_password_entry.get().strip()
        if not master_password:
            messagebox.showwarning("Missing Password", "Enter the master password first.")
            return

        data = load_data(master_password)
        if data is None:
            messagebox.showerror(
                "Unlock Failed",
                "Unable to decrypt the vault. Check the master password and try again.",
            )
            return

        self.master_password = master_password
        self.data = data
        self.status_var.set(f"Vault unlocked. {len(self.data)} saved entries.")
        self._show_main_screen()

    def create_new_vault(self):
        master_password = self.unlock_password_entry.get().strip()
        if not master_password:
            messagebox.showwarning(
                "Missing Password",
                "Enter a master password to create a new vault.",
            )
            return

        confirm_password = simpledialog.askstring(
            "Confirm Master Password",
            "Re-enter the master password for the new vault:",
            show="*",
            parent=self.root,
        )

        if confirm_password is None:
            return

        if master_password != confirm_password:
            messagebox.showerror("Password Mismatch", "The passwords do not match.")
            return

        should_continue = messagebox.askyesno(
            "Create New Vault",
            "Creating a new vault will overwrite existing saved data the next time you save. Continue?",
        )
        if not should_continue:
            return

        self.master_password = master_password
        self.data = {}
        self.status_var.set("New vault ready. Add entries and save when you are done.")
        self._show_main_screen()

    def refresh_entries(self):
        for item in self.entry_tree.get_children():
            self.entry_tree.delete(item)

        for service, username, _password in list_entries(self.data, self.search_var.get()):
            self.entry_tree.insert("", "end", values=(service, username))

    def on_entry_selected(self, _event=None):
        selection = self.entry_tree.selection()
        if not selection:
            return

        service = self.entry_tree.item(selection[0], "values")[0]
        credentials = get_entry(self.data, service)
        if not credentials:
            return

        self.service_var.set(service)
        self.username_var.set(credentials["username"])
        self.password_var.set(credentials["password"])

    def toggle_password_visibility(self):
        self.password_entry.configure(show="" if self.show_password_var.get() else "*")

    def save_entry(self):
        service = self.service_var.get().strip()
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not service or not username or not password:
            messagebox.showwarning(
                "Missing Information",
                "Service, username, and password are all required.",
            )
            return

        service_exists = service in self.data
        if service_exists:
            should_update = messagebox.askyesno(
                "Update Entry",
                f"An entry for '{service}' already exists. Update it?",
            )
            if not should_update:
                return

        try:
            set_entry(self.data, service, username, password)
        except ValueError as error:
            messagebox.showerror("Invalid Entry", str(error))
            return

        self.refresh_entries()
        self.status_var.set(f"Entry for '{service}' saved.")
        self._select_service(service)

    def remove_entry(self):
        service = self.service_var.get().strip()
        if not service:
            messagebox.showwarning("No Entry Selected", "Select or enter a service to delete.")
            return

        if service not in self.data:
            messagebox.showinfo("Not Found", f"No entry found for '{service}'.")
            return

        should_delete = messagebox.askyesno(
            "Delete Entry",
            f"Delete the entry for '{service}'?",
        )
        if not should_delete:
            return

        delete_entry(self.data, service)
        self.refresh_entries()
        self.clear_form()
        self.status_var.set(f"Entry for '{service}' deleted.")

    def clear_form(self):
        self.service_var.set("")
        self.username_var.set("")
        self.password_var.set("")
        selection = self.entry_tree.selection()
        if selection:
            self.entry_tree.selection_remove(*selection)

    def _select_service(self, service):
        for item in self.entry_tree.get_children():
            values = self.entry_tree.item(item, "values")
            if values and values[0] == service:
                self.entry_tree.selection_set(item)
                self.entry_tree.focus(item)
                self.entry_tree.see(item)
                break

    def save_vault(self):
        if not self.master_password:
            messagebox.showwarning("Vault Locked", "Unlock the vault before saving.")
            return

        save_data(self.data, self.master_password)
        self.status_var.set("Vault saved successfully.")
        messagebox.showinfo("Saved", "Your encrypted vault has been saved.")

    def change_master_password(self):
        if not self.master_password:
            return

        current_password = simpledialog.askstring(
            "Current Password",
            "Enter the current master password:",
            show="*",
            parent=self.root,
        )
        if current_password is None:
            return

        if current_password != self.master_password:
            messagebox.showerror("Incorrect Password", "The current master password is incorrect.")
            return

        new_password = simpledialog.askstring(
            "New Master Password",
            "Enter a new master password:",
            show="*",
            parent=self.root,
        )
        if new_password is None:
            return

        new_password = new_password.strip()
        if not new_password:
            messagebox.showerror("Invalid Password", "The new master password cannot be empty.")
            return

        confirm_password = simpledialog.askstring(
            "Confirm Password",
            "Re-enter the new master password:",
            show="*",
            parent=self.root,
        )
        if confirm_password is None:
            return

        if new_password != confirm_password.strip():
            messagebox.showerror("Password Mismatch", "The passwords do not match.")
            return

        self.master_password = new_password
        save_data(self.data, self.master_password)
        self.status_var.set("Master password changed and vault re-encrypted.")
        messagebox.showinfo("Success", "Master password changed successfully.")

    def on_close(self):
        if self.master_password:
            should_save = messagebox.askyesnocancel(
                "Save Before Exit",
                "Do you want to save the vault before closing?",
            )

            if should_save is None:
                return

            if should_save:
                save_data(self.data, self.master_password)

        self.root.destroy()


def main():
    root = tk.Tk()
    style = ttk.Style()
    if "clam" in style.theme_names():
        style.theme_use("clam")

    PasswordManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
