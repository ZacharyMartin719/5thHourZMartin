#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW23
import random
import time
#1. Import the random and time libraries

#2. Create a class containing a def function that inits self and the 3 attributes health, damage, and speed.
class Charc:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def damage_1(self):
         for i in range(1,10):
             Warrior.health -= random.randint(1,6)
             time.sleep(1)
             print("The New Health is:", Warrior.health)
    def healer(self):
        Warrior.health += 30
        if Warrior.health >= 100:
            print(f"The new Health is at max health: {Warrior.health}")
        else:
            print(f"The Warriors Final Health is: {Warrior.health}")

#3. Make a "warrior" character object with 100 health, 20 damage, and 30 speed. Print the character's initial health below.
Warrior = Charc(100,20,30)
print(f"The Warrior Health is: {Warrior.health}")
#4. Make a def function within the class that loops 10 times. Within this function,
#make the following loop 10 times: the character takes a random amount of damage from 1 to 6,
#the new health is printed, a time.sleep delay of one second is done. Call the function to the warrior.
Warrior.damage_1()
#5. Make a "healer" character object with 60 health, 10 damage, and 30 speed.
healer = Charc(60,10,30)
#6. Make a def function within the class that heals the warrior for 30 health. Create an if statement
#that sets the warrior's health to its max (100) if the healing would bring the warrior's health above that.
#Call the function to the healer.
Warrior.healer()

#7. Print the warrior's final health at the very bottom.
print(Warrior.health)