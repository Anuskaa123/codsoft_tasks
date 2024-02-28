import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def percentage(x, y):
    return (x * y) / 100

def square_root(x):
    return math.sqrt(x)

def square(x):
    return x ** 2

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Percentage (%)")
    print("6. Square Root (√)")
    print("7. Square (x^2)")

    # Input
    num1 = float(input("Enter the first number: "))
    operation_choice = input("Choose an operation (1-7): ")

    if operation_choice in ('1', '2', '3', '4'):
        num2 = float(input("Enter the second number: "))

    # Perform calculation based on user's choice
    if operation_choice == '1':
        result = add(num1, num2)
        operator = '+'
    elif operation_choice == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif operation_choice == '3':
        result = multiply(num1, num2)
        operator = '*'
    elif operation_choice == '4':
        result = divide(num1, num2)
        operator = '/'
    elif operation_choice == '5':
        num2 = float(input("Enter the percentage value: "))
        result = percentage(num1, num2)
        operator = '% of'
    elif operation_choice == '6':
        result = square_root(num1)
        operator = '√'
    elif operation_choice == '7':
        result = square(num1)
        operator = '^2'
    else:
        print("Invalid operation choice.")
        return

    # Display result
    print(f"\nResult: {operator} {num1} = {result}")

# Run the calculator
calculator()
