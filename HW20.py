#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW20

#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    y = int(input("Pick a number"))
    x = 100/y
    print(x)

except:
    print("Can not divide by zero")

#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    i = int(input("Choose a number"))

except ValueError:
    print("Error")

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
c = 5
while c >= 0:
    print(c)
    c -= 1
    if c < 0:
        raise Exception("Raised")