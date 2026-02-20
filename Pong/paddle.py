from turtle import Turtle

MOVE_DISTANCE = 20
BOUNDARY = 280

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.paddle_h = 100
        self.paddle_w = 20
        self.speed("fastest")
    def move_up(self):
        self.setheading(90)
        if self.ycor() < BOUNDARY:
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(270)
        if self.ycor() > -BOUNDARY:
            self.forward(MOVE_DISTANCE)
