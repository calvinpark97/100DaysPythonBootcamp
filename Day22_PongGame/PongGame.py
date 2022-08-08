from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middleline import middleLine

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_on = True



rightPaddle = Paddle((350, 0))
leftPaddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
middleline = middleLine()

screen.listen()
screen.onkeypress(rightPaddle.MoveUp, "Up")
screen.onkeypress(rightPaddle.MoveDown, "Down")
screen.onkeypress(leftPaddle.MoveUp, "w")
screen.onkeypress(leftPaddle.MoveDown, "s")

while game_on == True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Detect Collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounceY()

    #Detect collision with right paddle
    if ball.distance(rightPaddle) < 100 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()
        ball.move_speed *= 0.9

    #Detect ball goes past
    if ball.xcor() > 350:
        score.leftPoint()
        ball.resetPosition()


    if ball.xcor() < -350:
        score.rightPoint()
        ball.resetPosition()


screen.exitonclick()