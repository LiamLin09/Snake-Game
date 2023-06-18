# create a snake body
# move the snake
# control the snake
# detect collision with food
# create a score board
# detect collision with wall
# detect collision with tail

from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    a = snake.head.xcor()
    b = snake.head.ycor()
    if a > 290 or a < -290 or b > 290 or b < -290:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    # if head collides with any segment in the tail:
    # trigger game_over
    for segment in snake.segments:
        if segment == snake.head:
            continue
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
