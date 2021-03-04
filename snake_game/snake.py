from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle("circle")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def reset_snake(self):
        for part in self.snake_parts:
            part.goto(1000, 1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        for part_index in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_index - 1].xcor()
            new_y = self.snake_parts[part_index - 1].ycor()
            self.snake_parts[part_index].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
