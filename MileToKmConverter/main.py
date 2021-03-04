from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=50, pady=50)


def calculate():
    converted_km = int(user_input.get()) * 1.609
    label_km.config(text=f"{converted_km}")


user_input = Entry(width=30)
user_input.grid(column=1, row=0)

label_mile = Label(text="Miles", font=("Arial", 15))
label_mile.grid(column=2, row=0)

label_is_equal_to = Label(text="is equal to", font=("Arial", 15))
label_is_equal_to.grid(column=0, row=2)

label_km = Label(text="0", font=("Arial", 15))
label_km.grid(column=1, row=2)

label_km_text = Label(text="Km", font=("Arial", 15))
label_km_text.grid(column=2, row=2)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()
