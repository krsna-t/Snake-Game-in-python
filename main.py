from turtle import *
import random
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
screen.delay(delay=None)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()


    #detect the collision of food with snake
    if snake.segment[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()



    #detect colllision with wall
    if (snake.segment[0].xcor() > 286 or snake.segment[0].xcor() < -286 or snake.segment[0].ycor() > 286 or snake.segment[0].ycor() < -286):
       game_is_on = False
       scoreboard.game_over()

    #detect collision with snake's tail 
    for segment in snake.segment:
        if segment == snake.segment[0]:
            pass
        elif snake.segment[0].distance(segment)<10:
            game_is_on= False
            scoreboard.game_over()

screen.exitonclick()