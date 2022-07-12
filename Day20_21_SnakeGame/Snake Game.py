from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
game_on = True
screen.tracer(0)

#generating the snake
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

while game_on == True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect eating/collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.point()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False

    #detect collision with tail
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            score.game_over()
            game_on = False

screen.exitonclick()