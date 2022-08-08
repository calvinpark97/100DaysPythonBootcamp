from turtle import Turtle
style_font = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        super().__init__()
        self.color("white")
        self.pu()
        self.goto(-20, 260)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=style_font)

    def point(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", 'w') as file:
                file.write(str(self.score))
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.highscore):
            with open("data.txt", 'w') as file:
                file.write(str(self.score))

        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("Game Over!", align="center", font=style_font)