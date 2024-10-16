#Name: Zachary Martin
#Class: 5th Hour
#Assignment: Scenario 3
import random

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

#Step 3: Make sure every enemy and party member has health points (fixed)
#Step 4: Make sure every enemy and party member has an attack modifier (fixed)
#Step 5: Make sure every enemy and party member has an armor class (AC) (fixed)
#Step 6: Make every enemy and party member has a damage roll (random)

#Step 1: Copy enemy dictionary from SC1.
enemyDict = {
    "Dominous": {
    "Health" : 11,
    "Damage" : random.randint(1,5),
    "Power" : "Ice/Freeze",
    "AC" : 16,
    "Attack Mod": 6,
},
    "Gabrious": {
       "Health" : 13,
       "Damage" : random.randint(2,6),
       "Power" : "Fire",
       "AC" : 15,
      "Attack Mod": 5,
 },
  "Rileyous": {
      "Health" : 15,
      "Damage" : random.randint(3,7),
      "Power" : "Electric",
      "AC" : 13,
      "Attack Mod": 5,
  },
   "Brentis": {
    "Health" : 11,
    "Damage" : random.randint(4,8),
    "Power" : "Strength",
    "AC" : 14,
    "Attack Mod" : 6,
},
    "Kevinous": {
    "Health" : 13,
    "Damage" : random.randint(5,9),
    "Power" : "Poison",
    "AC" : 12,
    "Attack Mod" : 7,
    },
}

#Step 2: Copy party dictionary from SC2

partyDict = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : random.randint(1,5),
        "Attack Mod": 6,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(2,6),
        "Attack Mod": 3,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : random.randint(3,7),
        "Attack Mod": 4,
    },

    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(4,8),
        "Attack Mod": 5,
    },
}

#Step 3: Make sure every enemy and party member has health points (fixed)
#Step 4: Make sure every enemy and party member has an attack modifier (fixed)
#Step 5: Make sure every enemy and party member has an armor class (AC) (fixed)
#Step 6: Make every enemy and party member has a damage roll (random)
#Here is the Code for the 20 sided dice
number = random.randint(1,20)
print('Press ENTER to roll the die.')
if input()=='':
	print(number)
#Party Dictionary Goes Here

#Enemy Dictionary Goes Here

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#Step 7: Pick a party member

#Step 8: Pick an ememy

#Step 9: Create an attack roll for party member

#Step 10: Compare the party member attack roll to the enemy AC

#Step 11: Subtract damage from enemy health if it hits

#Step 12: Check to see if enemy is still alive

#Step 13: Step 9 through 12, but enemy attacks party member if still alive

#Combat Code Goes Here.

if number >= enemyDict["Dominous"]["AC"]:
    enemyDict["Dominous"]["Health"] -= partyDict["LaeZel"]["Damage"]
    print("Sucess you got the hit, the enemy health is now", enemyDict["Dominous"]["Health"])
    if enemyDict["Dominous"]["Health"]<= 0:
        print("The enemy has fallen")
    else:
        print("Enemy is still alive")
else:
    print("Attack Missed")
if enemyDict["Dominous"]["Health"] > 0:
    number = random.randint(1,20) + enemyDict["Dominous"]["Attack Mod"]

    print('Press ENTER to roll the die to attack party members')

    if input() == '':
        print(number)

    if number >= partyDict["LaeZel"]["AC"]:
        partyDict["LaeZel"]["Health"] -= enemyDict["Dominous"]["Damage"]
        print("Successful hit")
        if partyDict["LaeZel"]["Health"]<= 0:
            print("Player has been defeated")

        else:
            print("The player is still alive")

    else:
        print("The attack was missed")