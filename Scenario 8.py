#Name: Zachary Martin
#Class: 5th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)
class Character:
    def __init__(self, name, am, health, damage, ac):
        self.name = name
        self.am = am
        self.health = health
        self.damage = damage
        self.ac = ac

Dominous = Character("Dominous", 5, 12, random.randint(3,8),14)
Gabrious = Character("Gabrious", 6 , 12, random.randint(2, 7), 15)
Rilryous = Character("Rileyous", 7, 12, random.randint(4, 9), 17)
Brentis = Character("Brentis", 8, 12, random.randint(1, 6), 12)
Kevinous = Character("Kevinous", 9, 12, random.randint(5, 11), 16)

LaeZel = Character("LaeZel", 7, 8, random.randint(1, 6), 17)
Shadowheart = Character("Shadowheart", 5, 19, random.randint(3, 8), 15)
Gale = Character("Gale", 6, 17, random.randint(1, 10), 13)
Astarion = Character("Astarion", 4, 12, random.randint(5, 10), 14)

if LaeZel.am >= Dominous.ac:
    Dominous.health -= LaeZel.damage
    print("Sucess you got the hit, the enemy health is now", Dominous.health)
    if Dominous.health <= 0:
        print("The enemy has fallen")
    else:
        print("Enemy is still alive")
else:
    print("Attack Missed")
if Dominous.health > 0:
    number = random.randint(1, 20) + Dominous.am

    print('Press ENTER to roll the die to attack party members')

    if input() == '':
        print(number)

    if number >= LaeZel.ac:
        LaeZel.health -= Dominous.damage
        print("Successful hit")
        if LaeZel.health <= 0:
            print("Player has been defeated")

        else:
            print("The player is still alive")

    else:
        print("The attack was missed")
