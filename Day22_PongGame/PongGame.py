from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
game_on = True
def moveUp():
    if rightPaddle.ycor() > 240:
        pass
    else:
        newy = rightPaddle.ycor() + 20
        rightPaddle.goto(350,newy)

def moveDown():
    if rightPaddle.ycor() < -230:
        pass
    else:
        newy = rightPaddle.ycor() - 20
        rightPaddle.goto(350,newy)

def LeftFlipperCreate():
    LeftFlipper = Turtle()
    LeftFlipper.shape('square')
    LeftFlipper.width(10)
    LeftFlipper.pu()
    LeftFlipper.goto(490, 0)

<<<<<<< HEAD
LeftFlipperCreate()
=======

rightPaddle = Turtle()
rightPaddle.ht()
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.turtlesize(5, 1)
rightPaddle.pu()
rightPaddle.ht()
rightPaddle.setpos(350,0)
rightPaddle.st()
screen.listen()
screen.onkeypress(moveUp, "Up")
screen.onkeypress(moveDown, "Down")

while game_on == True:
    screen.update()
    
screen.exitonclick()