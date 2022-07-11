from turtle import Turtle, Screen
from Snake import Snake
import time

screen = Screen()
screen.setup(width=500,height=500)
screen.bgcolor("black")
screen.title("Snake Game")
starting_position = [(0,0),(-20,0), (-40,0)]
game_on = True
screen.tracer(0)

#generating the snake
snake = Snake()
snake.create_snake()

while game_on == True:
    4snake.move()

screen.exitonclick()