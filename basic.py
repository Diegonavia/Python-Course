print("Welcome to this wonderful game :)")
print("...rock....")
print("...paper...")
print("...scissors...")

from random import choice
list = ["rock","paper","scissors"]

player_1 = input("Player 1 enter your choice\n").lower()
if player_1 != "":
    if player_1 == "rock" or player_1 == "paper" or player_1 == "scissors": 
        player_2 =(choice(list))
        print("The computer plays: \n" + player_2)
        if player_2 != "":
            if player_2 == "rock" or player_2 == "paper" or player_2 == "scissors":
                if player_1 == "rock" and player_2 == "paper":
                    print("Computer wins")
                elif player_1 == "rock" and player_2 == "scissors":
                    print("Player 1 wins")
                elif player_1 == "paper" and player_2 == "rock":
                    print("Player 1 wins")
                elif player_1 == "paper" and player_2 == "scissors":
                    print("Computer wins")
                elif player_1 == "scissors" and player_2 == "rock":
                    print("Computer wins")
                elif player_1 == "scissors" and player_2 == "paper":
                    print("Player 1 wins")
                elif player_1 == player_2:
                    print("You are tied, play again")
        
            else:
                print("Please enter a valid option")
        else:
            print("Please enter a valid option")

    else:
        print("Please enter a valid option")

else:
    print("Please enter a valid option")                

