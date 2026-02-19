from game_data import data
import random

## Functions for Game Play ## 
def remove_player(player):
    data.pop(data.index(player))

def start_game(players):
     total_players = len(data)
     a = random.randint(0,total_players)
     b = random.randint(0,total_players)
     if a == b:
         b = random.randint(0,total_players)
     players.append(data[a])
     players.append(data[b])
     data.pop(a)
     data.pop(b)
     return players

def next_player(players):
    players.append(random.choice(data))
    return players

def compare_followers(player1,player2):
    followers_a = player1.get('follower_count')
    followers_b = player2.get('follower_count')
    if followers_b > followers_a:
        return 'b'
    else:
        return 'a'

def increase_score(score):
    return score + 1

def move_to_front(players,winning_guess):
    if winning_guess == 'b':
        players.pop(0)
    else:
        players.pop(1)
    return players
### initial variables ###

current_match = []
current_score = 0
play_game = True
keep_going = True

print("Welcome to the Higher or Lower Game!")
current_match = start_game(current_match)


while play_game:
    print(f"Compare A: {current_match[0].get('name')}, a {current_match[0].get('description')} from {current_match[0].get('country')}")
    print(f"Compare B: {current_match[1].get('name')}, a {current_match[1].get('description')} from {current_match[1].get('country')}")
    winner = compare_followers(current_match[0],current_match[1])
    user_guess = input("Who has a higher follower count? 'A' or 'B': ").lower()
    if winner == user_guess:
        current_score = increase_score(current_score)
        print(f"Correct! Current Score: {current_score}")
        current_match = move_to_front(current_match,winner)
        current_match = next_player(current_match)
        remove_player(current_match[1])
    else:
        play_game = False
        print("Incorrect - Rerun program to play again.")

