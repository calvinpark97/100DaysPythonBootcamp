import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
level = Scoreboard()

screen.onkeypress(player.moveForward, "w")
loop_iteration = 0
cars.createCars()

game_is_on = True
while game_is_on:
    time.sleep(cars.levelSpeed)
    screen.update()
    loop_iteration += 1
    if loop_iteration == 8:
        cars.createCars()
        cars.moveCar()
        loop_iteration = 0
    if player.ycor() == 280:
        player.resetPosition()
        level.next_level()
        cars.nextLevel()
    for car in cars.createdCars:
        if car.distance(player)<20:
            level.you_lose()
            game_is_on = False

screen.exitonclick()
