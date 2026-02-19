from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")
TITLE_HEIGHT = 275

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(x=0,y=TITLE_HEIGHT)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", False, align = ALIGNMENT, font = FONT)


    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align = ALIGNMENT, font = FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT,font=FONT)

    

