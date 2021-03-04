from turtle import Screen
from player import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# screen of the game
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# listening to the key on the right side
screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)

# listening on the key on the left side
screen.onkey(key='w', fun=l_paddle.move_up)
screen.onkey(key='s', fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall in the  y axis
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with right paddle and the left paddle in the horizontal axis
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect when the right paddle misses the ball
    if ball.xcor() > 400:
        ball.restart()
        scoreboard.l_point()
    # detect when the left paddle misses the ball
    if ball.xcor() < -400:
        ball.restart()
        scoreboard.r_point()




screen.exitonclick()
