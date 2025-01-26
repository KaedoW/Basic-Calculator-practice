# Assisted by watsonx Code Assistant 

print("Welcome to the Calculator!")

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The result is:", num1 + num2)
    elif choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The result is:", num1 - num2)
    elif choice == "3":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("The result is:", num1 / num2)
    elif choice == "4":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The result is:", num1 * num2)
    elif choice == "5":
        break;
    else:
        print("Invalid choice! Please try again.")
