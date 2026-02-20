from turtle import Turtle, Screen

WIDTH = 1000
HEIGHT = 600
W_PADDING = 0.47
H_PADDING = 0.47
LEFT = (WIDTH *-W_PADDING,0)
RIGHT = (WIDTH *W_PADDING,0)

EASY_SPEED = .1
MEDIUM_SPEED = .06
HARD_SPEED = .02


def setup_field():
    turtle = Turtle()
    turtle.color("white")
    turtle.hideturtle()
    turtle.teleport(x=0,y=300)
    turtle.pencolor("white")
    turtle.pensize(5)
    turtle.speed("fastest")
    turtle.right(90)

    for i in range(20):
        turtle.forward(18)
        turtle.penup()
        turtle.forward(15)
        turtle.pendown()


def get_difficulty(screen):
    difficulty_map = {
    "1": EASY_SPEED,
    "2": MEDIUM_SPEED,
    "3": HARD_SPEED
}
    difficulty = None 
    while difficulty not in difficulty_map:
        difficulty = screen.textinput(
            "Select Difficulty",
            "Choose a difficulty level:\n\n"
            "1 - Easy\n"
            "2 - Medium\n"
            "3 - Hard\n\n"
            "Enter 1, 2, or 3:"
        )
    return difficulty_map[difficulty]


def get_target_score(screen):
    while True:
        user_input = screen.textinput(
            "Game Length",
            "Play until how many points?\n\n"
            "Enter a number between 1 and 21:"
        )

        if user_input and user_input.isdigit():
            value = int(user_input)
            if 1 <= value <= 21:
                return value