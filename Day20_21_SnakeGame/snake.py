from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

#creating the snake
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in starting_position:
            starting_snake = Turtle("square")
            starting_snake.color("white")
            starting_snake.pu()
            starting_snake.goto(position)
            self.snake_body.append(starting_snake)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            next_x = self.snake_body[seg_num - 1].xcor()
            next_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(next_x, next_y)
        self.snake_body[0].forward(move_distance)

    def Up(self):
        self.snake_body[0].seth(90)


    def Down(self):
        self.snake_body[0].seth(270)


    def Left(self):
        self.snake_body[0].seth(180)


    def Right(self):
        self.snake_body[0].seth(0)
