print("Welcome to this wonderful game :)")
print("...rock....")
print("...paper...")
print("...scissors...")

import random
list = ["rock","paper","scissors"]

player_1 = input("Player 1 enter your choice\n")
player_2 = print(random.choice(list))
        
               
if player_1 == player_2:
    print("it's tied")
elif player_1 == "rock":
    if player_2 == "paper":
        print("Player 2 wins")
    elif player_2 == "scissors":
        print("Player 1 wins")
elif player_1 == "paper":
    if player_2 == "rock":
        print("Player 1 wins")
    elif player_2 == "scissors":
        print("Player 2 wins")
elif player_1 == "scissors":
    if player_2 == "rock":
        print("Player 2 wins")
    elif player_2 == "paper":
        print("Player 1 wins")

                





              