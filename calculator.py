# # Calculator using while with condition
# Functions to perform operations

# Addition

def add(a, b): 
    return a + b

# Subtraction

def sub(a, b):
    return a - b
# Multiplication

def multiply(a, b):
    return a * b
# Division
def divide(a, b):
    return "Cannot divide by zero" if b == 0 else a / b
# Average
def avg(a, b): 
    return (a + b) / 2
# Taking user input
choice = 0
while choice != 6:
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Average")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 6:
        print("Exiting the calculator")
        break
    if choice < 1 or choice > 6:
        print("Invalid choice.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", sub(a, b))
    elif choice == 3:
        print("Result:", multiply(a, b))
    elif choice == 4:
        print("Result:", divide(a, b))
    elif choice == 5:
        print("Result:", avg(a, b))
