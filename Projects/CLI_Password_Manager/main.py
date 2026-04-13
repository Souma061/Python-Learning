from getpass import getpass
from manager import load_data, save_data, add_entry, view_entries, search_entries


def unlock_data():
    while True:
        master_pass = getpass("Enter your master password: ")
        data = load_data(master_pass)

        if data is not None:
            return master_pass, data

        print("\nUnable to unlock existing data.")
        action = input("Choose: [R]etry, [N]ew vault (reset), [Q]uit: ").strip().lower()

        if action == "r":
            continue
        if action == "n":
            print("Starting a new empty vault. Existing encrypted data will be overwritten on save.")
            return master_pass, {}
        if action == "q":
            return None, None

        print("Invalid choice. Please choose R, N, or Q.")


def change_master_password(data, current_master_pass):
    current_input = getpass("Enter current master password: ")
    if current_input != current_master_pass:
        print("Current master password is incorrect.")
        return current_master_pass

    new_master_pass = getpass("Enter new master password: ")
    if not new_master_pass:
        print("New master password cannot be empty.")
        return current_master_pass

    confirm_pass = getpass("Confirm new master password: ")
    if new_master_pass != confirm_pass:
        print("Passwords do not match. Master password was not changed.")
        return current_master_pass

    save_data(data, new_master_pass)
    print("Master password changed successfully.")
    return new_master_pass


def main():
    print("Welcome to the Password Manager")
    master_pass, data = unlock_data()

    if master_pass is None:
        return

    while True:
        print("\nOptions: ")
        print("1. Add new entry")
        print("2. View entries")
        print("3. Search entries")
        print("4. Change master password")
        print("5. Save and exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_entry(data)
        elif choice == "2":
            view_entries(data)
        elif choice == "3":
            search_entries(data)
        elif choice == "4":
            master_pass = change_master_password(data, master_pass)
        elif choice == "5":
            save_data(data, master_pass)
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
