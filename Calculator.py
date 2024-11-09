def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    print("Simple Calculator")
    
    # User input for numbers and operation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        operation = input("Enter choice (1/2/3/4): ")

        if operation == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Invalid input! Please select a valid operation.")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Run the calculator
main()
