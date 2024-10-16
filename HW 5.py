#Name: Zachary Martin
#Class: 5TH Hr
#Assignment: HW5

#1. Print "Hello World!"
print("Hello World!")

#2. Create a list that contains 3 integers
numList=[3,7,5]

#3. Create an if statement that prints out whichever of the three numbers is the highest

if numList[0] > numList[1] and numList[0] > numList[2]:
    print("The biggest number is the first number.")

elif numList[1] > numList[0] and numList[1] > numList[2]:
    print("The second number is the biggest number.")

else:
    print("The third number is the biggest number.")

print(numList)