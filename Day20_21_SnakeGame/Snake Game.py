from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
game_on = True
screen.tracer(0)

#generating the snake
snake = Snake()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

while game_on == True:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()