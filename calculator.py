# LEVEL UP! Bonus Challenge
# Challenge: Build a Basic Calculator


def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    return "Error: Anything divided by 0 is 0!" if b == 0 else a / b

def calculator():
    print("Welcome to the Calculator!")
    print("Choose operation: add, subtract, multiply, divide")

    operation = input("Enter operation: ").lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "add":
        print("Result:", add(a, b))
    elif operation == "subtract":
        print("Result:", subtract(a, b))
    elif operation == "multiply":
        print("Result:", multiply(a, b))
    elif operation == "divide":
        print("Result:", divide(a, b))
    else:
        print("Invalid operation.")


calculator()


