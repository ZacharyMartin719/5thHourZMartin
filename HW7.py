#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")

#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = True
admin = True

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
users = 0

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True:
    if login == True:
        if admin == True:
            print("Hello User!")
            users += 2
        else:
            print("Error, you're missing admin access.")
    else:
        print("Error, you're missing your login.")
else:
    print("Error, you ain't connected to the wifi. ")

print(users)
