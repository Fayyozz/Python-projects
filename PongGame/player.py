from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.coordinate = coordinate
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        self.goto(coordinate)
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5, outline=1)

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)