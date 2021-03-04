from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    ent_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = ent_website.get().lower()
    email = ent_email.get()
    password = ent_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields", message="Please do not leave fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old file
                data = json.load(data_file)

        except FileNotFoundError:
            # Creating the file if there is no file
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating the existing file with the new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            ent_website.delete(0, END)
            ent_password.delete(0, END)

def find_password():
    website_entered = ent_website.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No file", message="Not Data File Found!")
    else:
        if website_entered in data:
            details_of_website = data.get(website_entered)
            messagebox.showinfo(title=website_entered.title(), message=f"Email: {details_of_website['email']} \n Password: {details_of_website['password']}")
        else:
            messagebox.showinfo(title=website_entered, message=f"No details for the {website_entered} found!")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="PasswordGenerator.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Creating labels GUI
lbl_website = Label(text="Website:", font=("Arial", 15, "normal"))
lbl_website.grid(column=0, row=1)
lbl_email = Label(text="Email/Username:", font=("Arial", 15, "normal"))
lbl_email.grid(column=0, row=2)
lbl_password = Label(text="Password:", font=("Arial", 15, "normal"))
lbl_password.grid(column=0, row=3)

# Creating entry input forms for the GUI
ent_website = Entry(width=30)
ent_website.grid(column=1, row=1, columnspan=2)
ent_website.focus()
ent_email = Entry(width=35)
ent_email.grid(column=1, row=2, columnspan=2)
ent_email.insert(0, "fayyozbek@gmail.com")
ent_password = Entry(width=21)
ent_password.grid(column=1, row=3)

# Creating buttons for the GUI
btn_generate_password = Button(text="Generate Password", command=generate_password)
btn_generate_password.grid(column=2, row=3)
btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(column=1, row=4, columnspan=2)
btn_search = Button(text="Search", width=10, command=find_password)
btn_search.grid(column=3, row=1)


window.mainloop()
