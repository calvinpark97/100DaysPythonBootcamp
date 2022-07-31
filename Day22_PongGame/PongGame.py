from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=1000,height=800)
screen.bgcolor("black")
screen.title("Pong")
game_on = True
screen.tracer(0)

def LeftFlipperCreate():
    LeftFlipper = Turtle()
    LeftFlipper.shape('square')
    LeftFlipper.width(10)
    LeftFlipper.pu()
    LeftFlipper.goto(490, 0)

LeftFlipperCreate()
screen.exitonclick()