from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?").lower()
colors = ("red", "orange", "yellow", "green", "blue", "violet")
y_pos = [-290, -60, -30,0, 30, 60, 290]

for turtles_color in range (0,6):
    Racing_Turtle = Turtle(shape="turtle")
    Racing_Turtle.color(colors[turtles_color])
    Racing_Turtle.pu()
    Racing_Turtle.goto(-230, y_pos[turtles_color])



screen.exitonclick()
