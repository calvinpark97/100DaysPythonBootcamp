from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.pu()
        self.ht()
        self.goto(-280, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def you_lose(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=FONT)
