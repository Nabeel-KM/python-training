print("This is a Calculator App")

toContinue = True

while toContinue:

    num1 = int(input("\nEnter First number : "))

    num2 = int(input("\nEnter Second number : "))

    print("Select the operation you want to perform./n")

    print("1.Addition")

    print("2.Subtraction")

    print("3.Multiplication")

    print("4.Division")

    print("5.Modulus/Remainder")

    choice = input("your choice : ")

    if choice == "1":
        result = num1 + num2
        print(f"Result of addition of {num1} and {num2} is {result}")
        print("\nAddition is performed")
        print("\nThank you for using this app")

    elif choice == "2":
        result = num1 - num2
        print(f"\nResult of subtraction of {num1} and {num2} is {result}")
        print("\nSubtraction is performed")
        print("\nThank you for using this app")

    elif choice == "3":
        result = num1 * num2
        print(f"Result of multiplication of {num1} and {num2} is {result}")
        print("\nMultiplication is performed")
        print("\nThank you for using this app")

    elif choice == "4":
        result = num1 / num2
        print(f"Result of division of {num1} and {num2} is {result}")
        print("\nDivision is performed")
        print("\nThank you for using this app")
    
    elif choice == "5":
        result = num1 % num2
        print(f"Result of modulus of {num1} and {num2} is {result}")
        print("\nModulus is performed")
        print("\nThank you for using this app")

    else:
        print("\nInvalid choice")

    userChoice = input ("\nDo you want to perform another calculation? (y/n) : ")

    if (userChoice == "n" or userChoice == "N"):
        toContinue = False
        print("\nThank you for using this app")
    