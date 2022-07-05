import random
from turtle import Turtle, Screen, colormode
from random import Random

Timmy = Turtle()
Timmy.shape("circle")
Timmy.color("white")
LoopOn = True
colormode(255)

#Box
#Timmy.speed(2)
#Timmy.forward(100)
#Timmy.right(90)
#Timmy.forward(100)
#Timmy.right(90)
#Timmy.forward(100)
#Timmy.right(90)
#Timmy.forward(100)
#Timmy.right(90)

#Dashed Lines
#for x in range(0,50):
#    Timmy.pd()
#    Timmy.forward(10)
#    Timmy.pu()
#    Timmy.forward(10)

#Shapes
#Square
#for x in range(4):
#   print(x)
#    Timmy.forward(50)
#    Timmy.right(90)

#Triangle
#for x in range(3):
#    Timmy.forward(50)
#    Timmy.right(120)

#pentagon
#for x in range(5):
#    Timmy.forward(50)
#    Timmy.right(72)

#hexagon
#for x in range(6):
#    Timmy.forward(50)
#    Timmy.right(60)

#heptagon
#for x in range(7):
#    Timmy.forward(50)
#    Timmy.right(51.43)

#Octagon
#for x in range(8):
#    Timmy.forward(50)
#    Timmy.right(45)

#nonagon
#for x in range(9):
#    Timmy.forward(50)
#    Timmy.right(40)

#decagon
#for x in range(10):
#    Timmy.forward(50)
#    Timmy.right(36)

#There is a way to create a function
#def Shapes():
#    for x in range(3,11):
#            for l in range(x):
#                TurnAngle = 360/x
#                Timmy.forward(50)
#                Timmy.right(TurnAngle)
#Shapes()


#Challenge 4 - Random walk
while LoopOn == True:
    Timmy.ht()
    Color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    Timmy.pencolor(Color)
    Timmy.pensize(10)
    Timmy.forward(30)
    MoveDirection = (random.choice([0, 90 , 180, 270]))
    Timmy.right(MoveDirection)

Screen = Screen()
Screen.exitonclick()