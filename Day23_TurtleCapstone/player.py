from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.shape("turtle")
        self.color("turquoise")
        self.lt(90)
        self.st()
        self.resetPosition()

    def resetPosition(self):
        self.goto(0, -260)

    def moveForward(self):
        self.position_y = self.ycor()
        self.position_y += 5
        self.goto(0, self.position_y)

