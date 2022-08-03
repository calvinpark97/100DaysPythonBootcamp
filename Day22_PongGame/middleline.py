from turtle import Turtle

class middleLine(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.goto(0, -300)
        self.pencolor("white")
        self.pensize(5)
        self.drawLines()

    def drawLines(self):
        for x in range(-300,300):
            if x % 20 == 0:
                self.pd()
                self.goto(0,x)
            else:
                self.pu()
                self.goto(0,x)
