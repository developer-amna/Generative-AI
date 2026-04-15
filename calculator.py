import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def square_root(a):
    if a < 0:
        return "Error! Negative number."
    return math.sqrt(a)

def exponent(a, b):
    return a ** b

def log_value(a):
    if a <= 0:
        return "Error! Log undefined."
    return math.log(a)   # natural log (ln)


while True:
    print("\n--- Advanced Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponent (a^b)")
    print("7. Log (ln)")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == '8':
        print("Calculator Closed ✅")
        break

    # Two-number operations
    if choice in ['1', '2', '3', '4', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '6':
            print("Result:", exponent(num1, num2))

    # Single-number operations
    elif choice in ['5', '7']:
        num = float(input("Enter number: "))

        if choice == '5':
            print("Result:", square_root(num))
        elif choice == '7':
            print("Result:", log_value(num))

    else:
        print("Invalid choice! Try again.")