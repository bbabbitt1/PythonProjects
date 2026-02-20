from turtle import Turtle
import math
import random

MOVE_DISTANCE = 20 
INCREMENT = 10 
BOUNDARY = 290
SPEED = 10

class Puck(Turtle):
    def __init__(self):
       super().__init__()
       self.shape("square")
       self.penup()
       self.color("white")
       self.x_move = SPEED
       self.y_move = SPEED
    
    def tip_off(self):
        self.goto(0,0)
        not_Valid = True
        while not_Valid:
            angle = random.randint(0,359)
            if not (80 < angle < 100) and not (260 < angle < 280):
                not_Valid = False 
        self.x_move = SPEED * math.cos(math.radians(angle))
        self.y_move = SPEED * math.sin(math.radians(angle))
        self.goto(self.x_move,self.y_move)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
    
    def wall_bounce(self):
        self.y_move *= -1
    
    def paddle_bounce(self):
        self.x_move *= -1

