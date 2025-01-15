#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def rps_game():
    playerchoice = int(input("Choose 1 for Rock, 2 for Paper, and 3 Scissors"))
    opponentchoice = random.randint(1,3)

    print(f"Opponent got {opponentchoice}")
    if playerchoice == 1 and opponentchoice == 2:
        print("opponent won with paper over your rock.")

    elif playerchoice == 1 and opponentchoice == 2:
        print("Opponents Paper won")
    elif playerchoice == 1 and opponentchoice == 3:
        print("You won against Scissors with your Rock")
    elif playerchoice == 2 and opponentchoice == 1:
        print("Your Paper won over there Rock")
    elif playerchoice == 2 and opponentchoice == 3:
        print("Opponents Scissors won")
    elif playerchoice == 3 and opponentchoice == 1:
        print("Opponents Scissors won")
    elif playerchoice == 3 and opponentchoice == 2:
        print("Your Scissors won")
    elif playerchoice == 1 and opponentchoice == 1:
        print("Tie")
    elif playerchoice == 2 and opponentchoice == 2:
        print("Tie")
    elif playerchoice == 3 and opponentchoice == 3:
        print("Tie")
    else:
        print("Invalid number please choose a different number")
        rps_game()
    replay_rps()

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def replay_rps():
    replayInput = input("Do you wanna play again? Y/N ")

    if replayInput == "Y" or replayInput == "y":
        rps_game()
    elif replayInput == "N" or replayInput == "n":
        exit()

    else:
        print("Invalid input")
        replay_rps()

rps_game()