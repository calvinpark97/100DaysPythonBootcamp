from turtle import Turtle, Screen

Timmy = Turtle()
screen = Screen()


def move_forward():
    Timmy.forward(5)

def move_backward():
    Timmy.backward(5)

def turn_right():
    Timmy.right(5)

def turn_left():
    Timmy.left(5)

def screen_clear():
    screen.resetscreen()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkey(key="c", fun=screen_clear)

screen.exitonclick()