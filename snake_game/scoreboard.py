from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("../../Desktop/data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.write(f"Score: {self.score} Highest Score: {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
