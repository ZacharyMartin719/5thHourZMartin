#Name: Zachary Martin, Dom Acuna
#Class: 5th Hour
#Assignment: Scenario 5
import random
#Scenario 5
#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but there's only one problem:
#the same big wigs only bought enough computers for half of you. Because of this, you will
#all be split into teams of two. One serving as the brain (not using the computer),
#one serving as the hands (using the computer).

#The Teams are as such:

#Team 1: Dom (brain), Zachary (hand)
#Team 2: Ryley (brain), Ethan W (hand)
#Team 3: Eli (brain), Preston (hand)
#Team 4: Gabe (brain), Quinn (hand)
#Team 5: Sam (brain), Chaysen (hand)
#Team 6: Kevin (brain), Ethan M (hand)
#Team 7: Gage (brain), Eric (hand)

#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.

#RedNeck Roulette

roulette_wheel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
money = 100

# Ask how many rounds the user wants to play
rounds = int(input("How many times would you like to play? "))

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}: You have ${money}.")

# Get input for color choice
    choice = int(input("Pick a color (1 for Green, 2 for Red, 3 for Black): "))
    bet_amount = int(input(f"How much do you want to bet? (You have ${money}): "))

# Make sure you have enough money for the amount you wanna bet
    if bet_amount > money:
        print("You don't have enough money for that.")
        continue

# Spin the roulette wheel
    spin_result = random.choice(roulette_wheel)
    print(f"The result is: {spin_result}")

# Determine the color of the result
    if spin_result == 0:
        print("The color is Green.")
        result_color = 1
    elif spin_result % 2 == 0:
        print("The color is Red.")
        result_color = 2
    else:
        print("The color is Black.")
        result_color = 3

# Check if you guessed correctly
    if choice == result_color:
        print(f"Congratulations! You won ${bet_amount}.")
        money += bet_amount
    else:
        print(f"Sorry, you lost ${bet_amount}.")
        money -= bet_amount

# When you run outta money
    if money <= 0:
        print("You're out of money! Game over.")
        break

# State how much money you have left
print(f"\nGame over. You have ${money} left.")