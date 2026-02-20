from turtle import Turtle
import random 

UPPER_BOUND = 280
LOWER_BOUND = -280


class Food(Turtle):
    
    def __init__(self):
       super().__init__()
       self.shape("circle")
       self.penup()
       self.shapesize(stretch_len=.5,stretch_wid=.5)
       self.color("blue")
       self.speed("fastest")
       rand_x = random.randint(LOWER_BOUND,UPPER_BOUND)
       rand_y = random.randint(LOWER_BOUND,UPPER_BOUND)
       self.goto(rand_x, rand_y)

    def new_position(self):
        x_cord = random.randint(LOWER_BOUND,UPPER_BOUND)
        y_cord = random.randint(LOWER_BOUND,UPPER_BOUND)
        self.goto(x=x_cord,y=y_cord)
    