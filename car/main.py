import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = []


# initializing the player class
player = Player()
scoreboard = Scoreboard()
for _ in range(40):
    car_manager = CarManager()
    cars.append(car_manager)


# listening to the key strokes
screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:

        # collision with the car
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

        car.move_car()
        # moving the car go back again when reached to the end
        if car.xcor() <= -300:
            car.go_back()

    # setting the player to the starting position when reached top
    if player.ycor() >= 280:
        player.start_up()
        scoreboard.update_level()

        for car in cars:
            car.increase_speed()


screen.exitonclick()
