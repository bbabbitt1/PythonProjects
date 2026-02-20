from turtle import Turtle

PLAYER_1_X = -50
PLAYER_2_X = 50
SCORE_Y = 240
FONT = ("Courier New", 40, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()
 
    def update_score(self):
        self.clear()
        self.goto(x=PLAYER_1_X, y =SCORE_Y)
        self.write(self.left_score, False, align = "left", font = FONT)
        self.goto(x=PLAYER_2_X, y =SCORE_Y)
        self.write(self.right_score, False, align = "right", font = FONT)
    
    def point_left(self):
        self.left_score += 1
        self.update_score()

    def point_right(self):
        self.right_score += 1
        self.update_score()
    
    def announce_winner(self):
        self.goto(0, 0)
        self.color("blue")
        if self.left_score > self.right_score:
            self.write("Left Player Wins!", align="center", font=FONT)
        else:
            self.write("Right Player Wins!", align="center", font=FONT)

