from turtle import Turtle
style_font = ('Courier', 50, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.leftScore = 0
        self.rightScore = 0
        self.color("white")
        self.pu()
        self.goto(-20, 240)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f" {self.leftScore}   {self.rightScore}", align="center", font=style_font)

    def leftPoint(self):
        self.leftScore += 1
        self.clear()
        self.update_scoreboard()

    def rightPoint(self):
        self.rightScore += 1
        self.clear()
        self.update_scoreboard()