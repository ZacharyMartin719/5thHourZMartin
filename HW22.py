#Name: Zachary Martin
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Store:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double(self):
        self.cost *= (2)
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
rice = Store(45, 6.35, 3)
beans = Store(35, 5.99, 4)
bread = Store(20, 4.50, 2)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"The stock of Rice is: {rice.stock}")
print(f"The stock of Beans is: {beans.stock}")
print(f"The stock of Bread is: {bread.stock}")

print(f"The cost of Beans is: {beans.cost}")
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
beans.double()
print("This doubles the price",beans.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
bread.stock = 5
print("The new stock number for bread is:", bread.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del rice

try:
    print(rice.weight)

except:
    print("Item not found")