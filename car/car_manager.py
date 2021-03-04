from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT
        self.penup()
        random_color = random.randint(0, len(COLORS) - 1)
        self.color(COLORS[random_color])
        self.random_pos()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape('square')

    def random_pos(self):
        random_x = random.randint(300, 900)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)

    def move_car(self):
        self.forward(self.move_distance)

    def go_back(self):
        if self.xcor() <= -300:
            self.random_pos()

    def increase_speed(self):
        self.move_distance += self.move_increment

