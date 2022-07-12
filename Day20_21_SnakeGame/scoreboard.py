from turtle import Turtle
style_font = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.pu()
        self.goto(-20, 260)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=style_font)

    def point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=style_font)