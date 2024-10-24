#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World!")

import random

#2. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

#if temp > 20
#   yes its hot
#   no is it greater than 10
#   yes its mild
# no its cold

temp = random.randint (0,30)

print(temp)

if temp > 20:
    print("It's hot ")
elif temp > 10:
        print("Its mild")
else:
     print("It's cold")
print("Thank you!")