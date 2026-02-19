from turtle import Turtle, Screen

STARTING_X = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):   
        for position in STARTING_X:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment) 

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1, 0,-1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def move_up(self):
        
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.move()
        else:
            self.move()
        
    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.move()
        else:
            self.move()

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.move()
        else:
            self.move()
    
    def turn_right(self):
        if self.head.heading() != 180: 
            self.head.setheading(0)
            self.move()
        else:
            self.move()

    

