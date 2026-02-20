from turtle import Turtle, Screen
from puck import Puck
from score import Scoreboard
from paddle import Paddle
import time
from config import setup_field, get_difficulty, get_target_score, WIDTH, HEIGHT, LEFT, RIGHT, H_PADDING, W_PADDING




screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height = HEIGHT)
screen.title("Pong")
screen.tracer(0)

setup_field()
puck = Puck()
scoreboard = Scoreboard()

left_paddle = Paddle(LEFT)
right_paddle = Paddle(RIGHT)


game_speed = get_difficulty(screen)
target_score = get_target_score(screen)

screen.listen()
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down,"Down")
screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down,"s")


puck.tip_off()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(game_speed)
    puck.move()

    if puck.ycor() > HEIGHT * H_PADDING or puck.ycor() < -HEIGHT * H_PADDING:
        puck.wall_bounce()
    
    for paddle in [left_paddle, right_paddle]:
        if (abs(puck.xcor() - paddle.xcor()) < paddle.paddle_w and 
            abs(puck.ycor() - paddle.ycor()) < paddle.paddle_h):
            puck.paddle_bounce()

    if puck.xcor() > WIDTH *W_PADDING:
        scoreboard.point_left()
        puck.tip_off()

    if puck.xcor() < WIDTH *-W_PADDING:
        scoreboard.point_right()
        puck.tip_off()
    
    if scoreboard.left_score == target_score or scoreboard.right_score == target_score:
        scoreboard.announce_winner()
        game_is_on = False

screen.exitonclick()