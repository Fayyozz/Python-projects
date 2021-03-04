from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():

    window.after_cancel(timer)
    global timer_text
    canvas.itemconfig(timer_text, text="00:00")
    lbl_timer.config(text="Timer", fg=GREEN)
    lbl_checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0

def start_timer():
    global reps
    reps += 1
    work_time_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        lbl_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        lbl_timer.config(text="Break", fg=PINK)
    else:
        count_down(work_time_secs)
        lbl_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_mins = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        checkmarks = ""
        for _ in range(math.floor(reps/2)):
            checkmarks += " ✔"
        lbl_checkmarks.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


lbl_timer = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
lbl_timer.grid(column=1, row=0)

lbl_checkmarks = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
lbl_checkmarks.grid(column=1, row=3)

btn_start = Button(text="Start", highlightthickness=0, command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
btn_reset.grid(column=2, row=2)


window.mainloop()