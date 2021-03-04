from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(-200, 250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Level {self.level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over", align="center", font=FONT)
