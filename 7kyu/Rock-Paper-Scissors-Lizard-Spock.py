#Description 
# In this kata, your task is to implement an extended version of the famous rock-paper-scissors game. The rules are as follows:

#     Scissors cuts Paper
#     Paper covers Rock
#     Rock crushes Lizard
#     Lizard poisons Spock
#     Spock smashes Scissors
#     Scissors decapitates Lizard
#     Lizard eats Paper
#     Paper disproves Spock
#     Spock vaporizes Rock
#     Rock crushes Scissors

# Task:

# Given two values from the above game, return the Player result as "Player 1 Won!", "Player 2 Won!", or "Draw!".
# Inputs

# Values will be given as one of "rock", "paper", "scissors", "lizard", "spock".
#MySolution
def rpsls(pl1, pl2):
    # Your Magnificent Code here
    win_dict = {"scissors": ("paper", "lizard"),
                "paper": ("rock", "spock"), 
                "rock": ("lizard", "scissors"), 
                "lizard": ("spock", "paper"), 
                "spock": ("scissors", "rock")}
    if pl2 in win_dict[pl1]:
        return "Player 1 Won!"
    elif pl1 in win_dict[pl2]:
        return "Player 2 Won!"
    elif pl1 == pl2:
        return "Draw!"