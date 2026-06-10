'''
Create a Python program that provides a menu to the user to select a 2D figure: Circle, Rectangle, or Square.

After selecting a figure, the user should enter the required input values (like radius, length, width, or side).

Then the program should again show a menu to select an operation:

Area
Perimeter

After performing the selected operation, display the result.

This process should repeat continuously for the selected figure until the user chooses to go back or exit.
'''


import math

while True:
    print("\n===== MAIN MENU =====")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    choice = int(input("Select a figure: "))

    # EXIT PROGRAM
    if choice == 4:
        print("Program Ended.")
        break

    # CIRCLE
    if choice == 1:
        radius = float(input("Enter radius of circle: "))

        while True:
            print("\n--- Circle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Back")

            op = int(input("Choose operation: "))

            if op == 1:
                area = math.pi * radius * radius
                print("Area of Circle =", area)

            elif op == 2:
                perimeter = 2 * math.pi * radius
                print("Perimeter of Circle =", perimeter)

            elif op == 3:
                break

    # RECTANGLE
    elif choice == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        while True:
            print("\n--- Rectangle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Back")

            op = int(input("Choose operation: "))

            if op == 1:
                print("Area of Rectangle =", length * width)

            elif op == 2:
                print("Perimeter of Rectangle =", 2 * (length + width))

            elif op == 3:
                break

    # SQUARE
    elif choice == 3:
        side = float(input("Enter side of square: "))

        while True:
            print("\n--- Square Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Back")

            op = int(input("Choose operation: "))

            if op == 1:
                print("Area of Square =", side * side)

            elif op == 2:
                print("Perimeter of Square =", 4 * side)

            elif op == 3:
                break

    else:
        print("Invalid choice! Please try again.")
        