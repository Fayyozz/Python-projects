THEME_COLOR = "#375362"
import tkinter
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_b = quiz_brain
        self.question_canvas = None
        self.window = tkinter.Tk()
        self.window.title("Quizler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = tkinter.Label(text=f"Score: 0", width=15, bg=THEME_COLOR, fg="white",
                                         font=('Arial', 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=500, height=400, bg="white")
        self.question_canvas = self.canvas.create_text(250, 200, width=450, text="Some text here",
                                                       font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tkinter.PhotoImage(file="./images/true.png")
        self.true_btn = tkinter.Button(image=true_image, command=self.answer_true)
        self.true_btn.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="./images/false.png")
        self.false_btn = tkinter.Button(image=false_image, command=self.answer_false)
        self.false_btn.grid(row=2, column=1)

        self.show_next_question()
        self.window.mainloop()

    def show_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_b.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_b.score}")
            q_text = self.quiz_b.next_question()
            self.canvas.itemconfig(self.question_canvas, text=q_text)
        else:
            self.false_btn.config(state="disabled")
            self.true_btn.config(state="disabled")
            self.canvas.itemconfig(self.question_canvas, text="You have reached the end of the quiz!")

    def answer_true(self):
        self.give_feedback(self.quiz_b.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz_b.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.show_next_question)




