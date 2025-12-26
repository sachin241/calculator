import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return math.pow(x, y)

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=math.e):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))  # input in degrees

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    return math.factorial(x)

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")

    choice = input("Enter choice (1-11): ")

    if choice in ['1','2','3','4','5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")

    elif choice == '6':
        num = float(input("Enter number: "))
        print(f"√{num} = {square_root(num)}")

    elif choice == '7':
        num = float(input("Enter number: "))
        base = input("Enter base (default e): ")
        base = float(base) if base else math.e
        print(f"log base {base} of {num} = {logarithm(num, base)}")

    elif choice == '8':
        angle = float(input("Enter angle in degrees: "))
        print(f"sin({angle}) = {sine(angle)}")

    elif choice == '9':
        angle = float(input("Enter angle in degrees: "))
        print(f"cos({angle}) = {cosine(angle)}")

    elif choice == '10':
        angle = float(input("Enter angle in degrees: "))
        print(f"tan({angle}) = {tangent(angle)}")

    elif choice == '11':
        num = int(input("Enter integer: "))
        print(f"{num}! = {factorial(num)}")

    else:
        print("Invalid input")

calculator()