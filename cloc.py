from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("CLOC")

# input field
entry = Entry(window, font=("Arial", 14))
entry.pack(pady=20)

# output label
label = Label(window, text="", font=("Arial", 14))
label.pack(pady=20)

# function to show input
def show_input():
    user_text = entry.get()
    label.config(text=user_text)

# button
button = Button(window, text="Submit", command=show_input)
button.pack()

window.mainloop()