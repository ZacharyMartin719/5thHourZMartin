#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW18
import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def print_hello():
    print("Hello World!")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["Red Bean", "Green Bean","Orange Bean","Brown Bean","White Bean"]

#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean_pull():
    if not beanBag:
        print("Bean Bag is empty.")
        exit()
    else:
        randombean = random.choice(beanBag)
        print(randombean)
        beanBag.remove(randombean)
    bean_question()

#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def bean_question():
    replayInput = input("Would you like to pick another Y/N ")

    if replayInput == "Y" or replayInput == "y":
        bean_pull()
    elif replayInput == "N" or replayInput == "n":
        exit()
    else:
        print("Invalid input")
        bean_yn()
#5. Call the #3 function at the bottom.
bean_pull()