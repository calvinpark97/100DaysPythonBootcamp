from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.pu()
        self.goto(position)

    def MoveUp(self):
        if self.ycor() > 230:
            pass
        else:
            newy = self.ycor() + 15
            self.goto(self.xcor(), newy)

    def MoveDown(self):
        if self.ycor() < -230:
            pass
        else:
            newy = self.ycor() - 15
            self.goto(self.xcor(), newy)





