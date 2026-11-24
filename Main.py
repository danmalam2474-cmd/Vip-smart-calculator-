
print("================================")
print("       VIP SMART CALCULATOR")
print("================================")

while True:
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using VIP Calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Try again.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Answer:", a + b)
    elif choice == "2":
        print("Answer:", a - b)
    elif choice == "3":
        print("Answer:", a * b)
    elif choice == "4":
        if b == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Answer:", a / b)
