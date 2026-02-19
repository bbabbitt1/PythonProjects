import random

## Game Play Functions ## 
def number_check(guess,correct_number,life):
    if guess == correct_number:
        print("You Win!")
    else:
        if guess > correct_number:
            print("Too high.\nGuess again.")
            return life - 1
        else:
            print("Too low. Guess again.")
            return life - 1
    if life == 0:
        print("You Lose.")

### initial variables ###

lives = 0
keep_guessing = True
play_game = True

#Start Game :) ###
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

correct_answer = random.randint(1, 100)
print(f"The correct number is {correct_answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("Invalid difficulty.")
while keep_guessing:
    print(f"You have {lives} remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    lives = number_check(user_guess,correct_answer,lives)
    if lives == 0 or user_guess == correct_answer:
        keep_guessing = False
        print("Refresh the page to play again!")
