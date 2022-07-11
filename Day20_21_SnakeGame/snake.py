from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
Up_direction = 90
Down_direction = 270
Left_direction = 180
Right_direction = 0

#creating the snake
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

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
        self.head.forward(move_distance)

    def Up(self):
        if self.head.heading() == Down_direction:
            pass
        else:
            self.head.seth(90)


    def Down(self):
        if self.head.heading() == Up_direction:
            pass
        else:
            self.head.seth(270)


    def Left(self):
        if self.head.heading() == Right_direction:
            pass
        else:
            self.head.seth(180)


    def Right(self):
        if self.head.heading() == Left_direction:
            pass
        else:
            self.head.seth(0)
