#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW10

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    i -= 1

else:
   print("Hello World!")

#2. Create a while loop that prints only even numbers
#between 1 and 30.
a = 1
while a <=30:
    a += 1
    if a % 2 == 0:
        print(a)

#3. Create a while loop that repeats until the user
#inputs the number 0.
b = int(input("Enter a number"))

while b != 0:
    if b == 0:
        break
    b = int(input("Wrong Number"))
