#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Charc:
    def __init__(self, health, damage, speed, max_health):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health = max_health
    def damage_1(self):
         for i in range(1,10):
             self.health -= random.randint(1,6)
             time.sleep(1)
             print("The New Health is:",self.health)
    def healer(self):
        self.health += 30
        if self.health >= 100:
            print(f"The new Health is at max health: {self.health}")
        else:
            print(f"The Warriors Final Health is: {self.health}")
#2. Create a fourth attribute in the class called max_health that has the same values as health
#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
Warrior = Charc(100, 20, 30,100)
healer = Charc(60, 10, 30,60)
thief = Charc(50, 30, 40,50)
mage = Charc(45, 35, 25,45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
x = random.randint(1,4)
if x == 1:
    Warrior.damage_1()
elif x == 2:
    healer.damage_1()
elif x == 3:
   thief.damage_1()
elif x == 4:
    mage.damage_1()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
if Warrior.health < Warrior.max_health:
    Warrior.healer()
    print("Warrior got hit his new health is", Warrior.health)
elif healer.health < healer.max_health:
    healer.healer()
    print("Healer got hit his new health is", healer.health)
elif thief.health < thief.max_health:
    thief.healer()
    print("thief got hit his new health is", thief.health)
elif mage.health < mage.max_health:
    mage.healer()
    print("mage got hit his new health is", mage.health)