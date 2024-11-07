#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW12

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.

for i in range(5, 0, -1):
    print(i)
print("Hello World!")

#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
for b in range(1,31):
    if b % 2 == 0:
        print(b)

#3. Create a for loop that prints 5 different animals from a list.
animals = ["Cow", "Pig", "Goat", "Dog","Coyote"]

for r in animals:
    print(r)

#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

for w in input()[::-1]:
    print(w)

