#  ______   ___   _______  _______    ______    _______  ___      ___        _______  _______  __   __  _______ 
# |      | |   | |       ||       |  |    _ |  |       ||   |    |   |      |       ||   _   ||  |_|  ||       |
# |  _    ||   | |       ||    ___|  |   | ||  |   _   ||   |    |   |      |    ___||  |_|  ||       ||    ___|
# | | |   ||   | |       ||   |___   |   |_||_ |  | |  ||   |    |   |      |   | __ |       ||       ||   |___ 
# | |_|   ||   | |      _||    ___|  |    __  ||  |_|  ||   |___ |   |___   |   ||  ||       ||       ||    ___|
# |       ||   | |     |_ |   |___   |   |  | ||       ||       ||       |  |   |_| ||   _   || ||_|| ||   |___ 
# |______| |___| |_______||_______|  |___|  |_||_______||_______||_______|  |_______||__| |__||_|   |_||_______|

# John Omoluabi

# This is a program which allows a group of players to roll a dice in turn. 
# The player whose accumulated dice rolls values come to a value greater then 50 wins

import random

def roll():
    max_value=6
    min_value=1
    value=random.randint(min_value, max_value)
    return value

# number of players
while True:
    players=input("enter the number of players(1-4): ")
    if players.isdigit():
        players=int(players)
        if 1 <= players <=4:
            break
    else:
        print("invalid entry")


max_score=50
player_scores=[0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("***************")
        print(f"passed to player {player_idx+1}")
        print("***************")
        s=0
        while True:
            should_roll=input("do you want to roll(y)? ")
            if should_roll != "y":
                break
            value=roll()
            if value==1 :
                print("pass!! you rolled a 1")
                break
            else:
                s+=value
                print(f"current score is {s}")

        player_scores[player_idx] += s
        print(f"total score is {player_scores[player_idx]}")

m=max(player_scores)
print(f"winner is {player_scores.index(m)+1}")
        

        
