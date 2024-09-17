#Name: Zachary Martin
#Class: 5TH Hr
#Assignment: Scenario 1

# Scenario 1:
# You are a programmer for a fledgling game developer. Your team lead
# has asked you to create a nested dictionary containing five enemy
# creatures (and their properties) for combat testing. Additionally,
# the testers are asking for a way to input changes to the enemy's
# damage for balancing, as well as having it print those changes to
# confirm they went through.
# It is up to you to decide what properties
# are important and the theme of the game.

#Enemy Character Dictionary
enemyDict = {
    "Dominous": {
    "Health" : 750,
    "Damage" : 70,
    "Power" : "Ice/Freeze"
},
    "Gabrious": {
       "Health" : 250,
       "Damage" : 50,
       "Power" : "Fire",
 },
  "Rileyous": {
      "Health" : 500,
      "Damage" : 300,
    "Power" : "Electric",
  },
   "Brentis": {
    "Health" : 175,
    "Damage" : 80,
    "Power" : "Strength"
},
    "Kevinous": {
    "Health" : 450,
    "Damage" : 125,
    "Power" : "Poison",
    },
}

#Print EnemyDict
print(enemyDict)

#New Damage for the Dominous
newDamageA = input("Enter new Damage Points for Dominous:")
enemyDict["Dominous"]["Damage"] = newDamageA

#New Damage for the Gabrious
newDamageB = input("Enter new Damage Points for Gabrious:")
enemyDict["Gabrious"]["Damage"] = newDamageB

#New Damage for the Rileyous
newDamageC = input("Enter new Damage Points for Rileyous:")
enemyDict["Rileyous"]["Damage"] = newDamageC

#New Damage for the Brentis
newDamageD = input("Enter new Damage Points for Brentis:")
enemyDict["Brentis"]["Damage"] = newDamageD

#New Damage for the Kevinous
newDamageE = input("Enter new Damage Points for Kevinous:")
enemyDict["Kevinous"]["Damage"] = newDamageE

#Print New Changes to the Damage Values to the Characters
print("Here are the New Damage Values to the Characters")
print(enemyDict)