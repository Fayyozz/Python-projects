
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"


# reading the csv file with pandas and getting dataFrame from it
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/russian_words.csv")

# converting the dataFrame to dictionary into list
list_of_words = df.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(list_of_words)
    canvas.itemconfig(language_name_text, text="Russian", fill="black")
    canvas.itemconfig(word_text, text=current_card["Russian"], fill="black")
    canvas.itemconfig(card_bg_image, image=card_front_img)
    flip_timer = window.after(3000, next_en_card)


def check_button():
    global list_of_words, current_card
    list_of_words.remove(current_card)
    new_df = pandas.DataFrame(list_of_words)
    new_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_en_card():
    canvas.itemconfig(card_bg_image, image=card_back_img)
    canvas.itemconfig(language_name_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# Window for the flash project
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, next_en_card)

# CANVAS CREATION:
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# background front card image
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
card_bg_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
# creating texts for the card
language_name_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Wrong button
image_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1)

# Right button
image_right = PhotoImage(file="./images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=check_button)
button_right.grid(column=1, row=1)

next_card()

window.mainloop()
