#Name: Zachary Martin
#Class: 5th hr
#Assignment: HW4

# 1. Print Hello World!
print("Hello World!")

# 2. Create a dictionary with 3 keys and a value for each key.
# One of the keys must have a value with a list containing
# three numbers inside
pickupDict = {
    "Brand" : "Ford",
    "Model" : "F-150",
     "Year" : [2024,2023,2022]
}

# 3. Print one of the three numbers by itself
print(pickupDict["Year"][2])

# 4. Using the update function, add a fourth key to the dictionary
# three numbers inside
pickupDict.update({"Package": "Lariat"})

# 5. Print the entire dictionary
print(pickupDict)

# 6. Clear all of the data inside of the dictionary and print it.
pickupDict.clear()
print(pickupDict)

# 7. Make a nested dictionary with three entries containing the name
# of another classmate and two other pieces of information within each entry.
fifthHour = {
    "student1": {
    "Name" : "Dom",
    "Grade" : 12,
    "Age" : 17,
},
    "student2": {
       "Name" : "Gabe",
       "Grade" : 12,
       "Age" : 17,
 },
  "student3": {
      "Name" : "Ryley",
      "Grade" : 11,
    "Age" : 17,
  }
}

# 8. Print the names of all three classmates on the same line.
print(fifthHour["student1"]["Name"],fifthHour["student2"]["Name"],fifthHour["student3"]["Name"])
