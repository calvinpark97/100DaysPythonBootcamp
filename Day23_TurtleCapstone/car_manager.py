from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.levelSpeed = 0.10
        self.direction_X = 10
        self.createdCars = []

    def createCars(self):
        randomStart = random.randint(-250, 250)
        newCar = Turtle()
        newCar.shape("square")
        newCar.pu()
        newCar.goto(250, randomStart)
        newCar.st()
        newCar.color(random.choice(COLORS))
        newCar.turtlesize(1, 2)
        self.createdCars.append(newCar)


    def moveCar(self):
        for car in self.createdCars:
            new_x = car.xcor() - self.direction_X
            current_y = car.ycor()
            car.goto(new_x, current_y)

    def nextLevel(self):
        self.levelSpeed *= 0.9