def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0 :
        return "Error : Cannot divide by 0"
    return a / b

operation = input("Which kind of operation ?(add/substract/mutiply/divide) : ")
a = float(input("Enter first number : "))
b = float(input("Enter second number : "))

if operation == "add" :
    print(f"Result: {add(a, b)}")

elif operation == "substract" :
    print(f"Result: {substract(a, b)}")
elif operation == "multiply" : 
    print(f"Result: {multiply(a, b)}")
    
else:
    print(f"Result: {divide(a, b)}")
   
