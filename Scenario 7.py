#Name: Zachary Martin
#Class: 5th Hour
#Assignment: Scenario 7
import random
#Import all of Scenario 6 here
from Scenario6 import stats
listAverage = 0

def final_average():
    global listAverage
    listAverage = average = sum(stats) / len(stats)
    print(f"Average Stat: {average:.2f}")#Calculate the sum of the list by the length of the list here
    return listAverage

final_average()
