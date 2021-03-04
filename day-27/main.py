from tkinter import *


def button_clicked():
    user_text = user_input.get()
    my_label.config(text=user_text)


window = Tk()
window.title("GUI first project")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = Label(text="This is label")
my_label.grid(column=0, row=0)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

user_input = Entry(width=30)
user_input.grid(column=3, row=2)


window.mainloop()
