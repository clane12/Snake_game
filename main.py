from turtle import *
import time
from snake import Snake
from food import Food
from score import *


screen = Screen()
screen.listen()
screen.setup(800, 600)
screen.bgcolor("black")

screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.onkey(fun=snake.turn_right, key="d")
    screen.onkey(fun=snake.turn_left, key="a")
    screen.onkey(fun=snake.turn_up, key="w")
    screen.onkey(fun=snake.turn_down, key="s")

    # collision between food and snake
    if snake.snakehead.distance(food) < 15:
        food.randon_location()
        score.incresesocre()
        snake.increase_snake()

    # detect collision with the wall
    if snake.snakehead.xcor() >= 400 or snake.snakehead.xcor() <= -400:
        score.highsc()
        snake.resetgame()
    elif snake.snakehead.ycor() >= 300 or snake.snakehead.ycor() <= -300:
        snake.resetgame()
        score.highsc()



    # detect collision with its tail
    # for segment in snake.snake:
    #     if segment == snake.snakehead:
    #         pass
    #     elif snake.snakehead.distance(segment) <= 5:
    #         score.gameover()
    #         game = False

    # for this code i used the slicing for the list which is done through [1:5] to go through 1 - 5
    # rather than starting from 0
    for segment in snake.snake[1:len(snake.snake)]:
        if snake.snakehead.distance(segment) <= 5:
            snake.resetgame()
            score.highsc()





screen.exitonclick()




