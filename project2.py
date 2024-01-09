def calculator():
    print("Welcome to the simple calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("\nSelect operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        print(f"The result is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result is: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    calculator()
