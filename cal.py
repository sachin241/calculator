import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def modulus(x, y): return x % y

def power(x, y): return math.pow(x, y)
def square_root(x): return math.sqrt(x)
def logarithm(x, base=math.e): return math.log(x, base)
def exponential(x): return math.exp(x)

def sine(x): return math.sin(math.radians(x))
def cosine(x): return math.cos(math.radians(x))
def tangent(x): return math.tan(math.radians(x))

def sinh(x): return math.sinh(x)
def cosh(x): return math.cosh(x)
def tanh(x): return math.tanh(x)

def deg_to_rad(x): return math.radians(x)
def rad_to_deg(x): return math.degrees(x)

def factorial(x): return math.factorial(x)
def percentage(x, y): return (x / y) * 100

memory = None
def store(val): 
    global memory
    memory = val
    return f"Stored {val} in memory."
def recall(): return memory if memory is not None else "Memory empty."
def clear_memory():
    global memory
    memory = None
    return "Memory cleared."

def calculator():
    print("\n--- Enhanced Scientific Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus")
    print("6. Power\n7. Square Root\n8. Logarithm\n9. Exponential")
    print("10. Sine\n11. Cosine\n12. Tangent")
    print("13. Sinh\n14. Cosh\n15. Tanh")
    print("16. Factorial\n17. Percentage")
    print("18. Degrees → Radians\n19. Radians → Degrees")
    print("20. Store in Memory\n21. Recall Memory\n22. Clear Memory")

    choice = input("Enter choice (1-22): ")

    if choice in ['1','2','3','4','5','6']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        ops = {
            '1': add, '2': subtract, '3': multiply, '4': divide,
            '5': modulus, '6': power
        }
        print("Result:", ops[choice](x, y))

    elif choice == '7':
        x = float(input("Enter number: "))
        print("Result:", square_root(x))

    elif choice == '8':
        x = float(input("Enter number: "))
        base = input("Enter base (default e): ")
        base = float(base) if base else math.e
        print("Result:", logarithm(x, base))

    elif choice == '9':
        x = float(input("Enter number: "))
        print("Result:", exponential(x))

    elif choice in ['10','11','12']:
        angle = float(input("Enter angle in degrees: "))
        funcs = {'10': sine, '11': cosine, '12': tangent}
        print("Result:", funcs[choice](angle))

    elif choice in ['13','14','15']:
        x = float(input("Enter number (radians): "))
        funcs = {'13': sinh, '14': cosh, '15': tanh}
        print("Result:", funcs[choice](x))

    elif choice == '16':
        x = int(input("Enter integer: "))
        print("Result:", factorial(x))

    elif choice == '17':
        x = float(input("Enter part value: "))
        y = float(input("Enter total value: "))
        print("Result:", percentage(x, y), "%")

    elif choice == '18':
        x = float(input("Enter degrees: "))
        print("Result:", deg_to_rad(x), "radians")

    elif choice == '19':
        x = float(input("Enter radians: "))
        print("Result:", rad_to_deg(x), "degrees")

    elif choice == '20':
        val = float(input("Enter value to store: "))
        print(store(val))

    elif choice == '21':
        print("Memory:", recall())

    elif choice == '22':
        print(clear_memory())

    else:
        print("Invalid choice!")
calculator()