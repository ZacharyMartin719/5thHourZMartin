#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW17


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def print_hello():
    print("Hello World!")


#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def flip_coin_100_times():
    global heads
    global tails
    for i in range(1, 101):
        coin_flip = random.randint(1,2)

        if coin_flip == 1:
            tails += 1

        else:
            heads += 1

#4. Call the "Hello world" and "Coin Flip" functions here
print_hello()
flip_coin_100_times()

#5. Print the final result of heads and tails here
print("This is how many times you flipped heads,", heads)
print("This is how many times you flipped tails,", tails)