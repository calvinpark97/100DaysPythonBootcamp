import turtle

import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
number_correct = 0
game_on = True

def name_animation(player_answer, xcor, ycor):
    answer = Turtle()
    answer.ht()
    answer.pu()
    answer.isvisible()
    answer.color('black')
    style = ('Arial', 10)
    answer.goto(xcor, ycor)
    answer.write(player_answer, move=True, font=style)

def find_coord(player_answer):
    state = states_list[states_list.state == player_answer]
    xcor = int(state.x)
    ycor = int(state.y)
    return(xcor, ycor)

states_list = pandas.read_csv('50_states.csv')
while game_on == True:
    player_answer = screen.textinput(title=f"{number_correct}/50Guess the state", prompt="Whats another state?")
    player_answer = player_answer.title()
    if (player_answer in states_list['state'].unique()):
        number_correct += 1
        xcor, ycor = find_coord(player_answer)
        name_animation(player_answer, xcor, ycor)

turtle.exitonclick()
