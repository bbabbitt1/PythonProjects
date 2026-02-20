from turtle import Screen 
from snake import Snake
from food import Food
from score import Scoreboard
import time

BOUNDARY = 280

screen = Screen()

screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    ### detect collision 
    if food.distance(snake.head) < 15:
        food.new_position()
        # ## add segment
        snake.extend()
        scoreboard.add_score()

    if snake.head.xcor() > BOUNDARY or snake.head.xcor() < -1 * BOUNDARY or snake.head.ycor()> BOUNDARY or snake.head.ycor() < -1 * BOUNDARY:
        scoreboard.game_over()
        game_is_on = False

    #Detect Collision with tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

    

    

        


## control the snake 

## detect collision with food 

## create a scoreboard

## detect collision with wall 

## detect collision with tail


screen.exitonclick()