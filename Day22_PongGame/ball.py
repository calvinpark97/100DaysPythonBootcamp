from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        print(self.speed())
        self.move_speed = 0.1
        self.directionx=10
        self.directiony=10

    def move(self):
        new_x = self.xcor() + self.directionx
        new_y = self.ycor() + self.directiony
        self.goto(new_x, new_y)

    def bounceY(self):
        self.directiony *= -1

    def bounceX(self):
        self.directionx *= -1

    def resetPosition(self):
        self.move_speed = 0.1
        self.goto(0,0)



