def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by 0"
    return a / b

operation = input("Which operation? (add/substract/multiply/divide): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == "add":
    print(f"Result: {add(a, b)}")
elif operation == "substract":
    print(f"Result: {substract(a, b)}")
elif operation == "multiply":
    print(f"Result: {multiply(a, b)}")
elif operation == "divide":
    print(f"Result: {divide(a, b)}")
else:
    print("Invalid operation! Please choose add, substract, multiply or divide.")
