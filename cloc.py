from tkinter import *


window = Tk()
window.geometry("520x380")
window.title("CLOC")


def count_lines():
    code_text = text_box.get("1.0", END).strip()
    code_lines = [line for line in code_text.splitlines() if line.strip()]

    if not code_text:
        result_label.config(text="Line count: 0")
        return

    result_label.config(text=f"Line count: {len(code_lines)}")


title_label = Label(window, text="Paste your code below", font=("Arial", 14))
title_label.pack(pady=(20, 10))

text_box = Text(window, font=("Arial", 12), width=50, height=12)
text_box.pack(padx=20, pady=10)

count_button = Button(window, text="Count Lines", command=count_lines, font=("Arial", 12))
count_button.pack(pady=10)

result_label = Label(window, text="Line count: 0", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()
