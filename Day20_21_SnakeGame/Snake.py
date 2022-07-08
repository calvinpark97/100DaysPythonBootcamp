from turtle import Turtle, Screen
import time

starting_position = [(0, 0), (-20, 0), (-40, 0)]

#creating the snake
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for start_coord in starting_position:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.pu()
            snake.goto(start_coord)
            self.snake_body.append(snake)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            next_x = self.snake_body[seg_num - 1].xcor()
            next_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(next_x, next_y)
            time.sleep(0.1)
        self.snake_body[0].forward(20)