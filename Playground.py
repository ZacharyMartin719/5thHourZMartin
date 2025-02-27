#Name: Zachary Martin
#Class: 5TH Hour
#Assignment: Playground
import random

print("Hello World!")
print("What is your name")
name=input()
print("Nice to meet you " + name + ".")
print(input("How are you doing today " + name +"."))
print("Great!")
#list1 = [1852,2345,5876,7908]
#list2 = [2890,1400,3456,8926]
#sum = list1[1] + list2[3]
#print(sum)

def user_input(money):
    rounds = int(input("How many times would you like to play? "))
    return rounds

def bet_amount(money):
    bet = int(input(f"How much do you want to bet? (You have ${money}): "))
    if bet > money:
        print("You don't have enough money for that.")
        return -1  # Indicate invalid bet
    return bet

def spin():
    roulette_wheel = list(range(37))  # Standard roulette wheel: 0-36
    spin_result = random.choice(roulette_wheel)
    print(f"The result is: {spin_result}")
    return spin_result

def pick_color(spin_result):
    if spin_result == 0:
        return 1  # Green
    elif spin_result % 2 == 0:
        return 2  # Red
    else:
        return 3  # Black

def check_win(choice, result_color, bet, money):
    if choice == result_color:
        print(f"Congratulations! You won ${bet}.")
        money += bet
    else:
        print(f"Sorry, you lost ${bet}.")
        money -= bet
    return money

def play_roulette():
    money = 100
    rounds = user_input(money)
    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}: You have ${money}.")
        choice = int(input("Pick a color (1 for Green, 2 for Red, 3 for Black): "))
        bet = bet_amount(money)
        if bet == -1:
            continue
        spin_result = spin()  # Get the result from spin function
        result_color = pick_color(spin_result)
        money = check_win(choice, result_color, bet, money)
        if money <= 0:
            print("You're out of money! Game over.")
            break
    print(f"\nGame over. You have ${money} left.")

play_roulette()

#Guessing Game
def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess it!")

    # Choose a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    attempts = 0

    while True:
        # Ask the user for their guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Check the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
            break

# Start the game
guess_the_number()
