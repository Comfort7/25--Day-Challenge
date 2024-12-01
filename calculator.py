import math
while True:
    try:
        print("\nAvailable operations: +, -, *, /, %, ^2, √")
        x = float(input("Enter a number of your choice: "))
        operation = input("Enter an operation: ").strip()
        
        if operation in ['^2', '√']:
            if operation == '^2':
                result = x ** 2
            elif operation == '√':
                if x < 0:
                    raise ValueError("Cannot calculate squareroot of a negative number")
                result = math.sqrt(x)
        else:          
            y = float(input("Enter another number of your choice: "))
        
            if operation == "+":
                result = x + y
            elif operation == "-":
                result = x - y
            elif operation == "/":
                if y == 0:
                    raise ValueError("Division by zero is not allowed!")
                else:
                    result = x / y  
            elif operation == "*":
                result = x * y
            elif operation == '%':
                result = (x * y) / 100
            else:
                raise ValueError("Invalid operation")

        print(f"The result of the operation is: {result}")
    except ValueError as e:
        print(f"An error occurred: {e}")
        
    again = input("Do you want to calculate again (yes/no)? ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break
        