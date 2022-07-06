import random
from turtle import Turtle, Screen, colormode

#Colorgram use
'''import colorgram
colorlist = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    colorlist.append(new_color)

print(colorlist)'''

colorlist = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
Hirst = Turtle()
Hirst.pensize(10)
colormode(255)
left_right = 0

for x in range(1, 102):
    random_color = random.choice(colorlist)
    Hirst.color(random_color)
    Hirst.dot()
    Hirst.pu()
    Hirst.forward(50)
    if x%10 == 0 and left_right == 0:
        Hirst.right(270)
        Hirst.forward(50)
        Hirst.right(270)
        left_right = 1
    elif x%10 == 0 and left_right == 1:
        Hirst.right(90)
        Hirst.forward(50)
        Hirst.right(90)
        left_right = 0

Screen = Screen()
Screen.exitonclick()