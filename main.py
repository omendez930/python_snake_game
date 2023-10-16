import random
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor('black')
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')




game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    #detects collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    #dtect collision with tail
    for segment in snake.segments[1:]:
        #bypasses snake head
        
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
    #if head collides with any segment in tail:
    #trigger game_over


















screen.exitonclick()