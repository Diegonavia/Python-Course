from random import choice

print("Welcome to this wonderful game :)")
player_wins = 0
computer_wins = 0
winning_score = 3
while player_wins < winning_score and player_wins < winning_score:
    print(f"Player Score {player_wins} Computer Score: {computer_wins}")
    print("...rock....")
    print("...paper...")
    print("...scissors...")

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
                        computer_wins += 1
                    elif player_1 == "rock" and player_2 == "scissors":
                        print("Player 1 wins")
                        player_wins += 1
                    elif player_1 == "paper" and player_2 == "rock":
                        print("Player 1 wins")
                        player_wins += 1
                    elif player_1 == "paper" and player_2 == "scissors":
                        print("Computer wins")
                        computer_wins += 1
                    elif player_1 == "scissors" and player_2 == "rock":
                        print("Computer wins")
                        computer_wins += 1
                    elif player_1 == "scissors" and player_2 == "paper":
                        print("Player 1 wins")
                        player_wins += 1
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

