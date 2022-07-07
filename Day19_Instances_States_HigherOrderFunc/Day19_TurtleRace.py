from turtle import Turtle, Screen
import random

screen = Screen()
race_on = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?").lower()
colors = ("red", "orange", "yellow", "green", "blue", "violet")
y_pos = [-100, -60, -20, 20, 60, 100]
Racing_Turtles = []

for turtles_color in range (0,6):
    New_Turtle = Turtle(shape="turtle")
    New_Turtle.color(colors[turtles_color])
    New_Turtle.pu()
    New_Turtle.goto(-230, y_pos[turtles_color])
    Racing_Turtles.append(New_Turtle)

if user_bet:
    race_on = True

while race_on == True:
    for x in range(0,6):
        turtle_speed = random.randint(0, 10)
        Racing_Turtles[x].forward(turtle_speed)
        if Racing_Turtles[x].xcor() > 250:
            winning_turtle = Racing_Turtles[x].fillcolor()
            race_on = False

if user_bet == winning_turtle:
    print(f"You win! The winning turtle color was {winning_turtle}!")
else:
    print(f"You lose! The winning turtle color was {winning_turtle}!")







screen.exitonclick()
