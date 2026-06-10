import math

def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side

def circle_area(radius):
    return math.pi * radius * radius

def circle_perimeter(radius):
    return 2 * math.pi * radius

while True:
    print("\n--- Select a 2D Figure ---")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:   # Circle
        r = float(input("Enter radius: "))
        while True:
            print("\n--- Circle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Circle Menu")
            op = int(input("Enter your choice: "))
            if op == 1:
                print("Area of Circle:", circle_area(r))
            elif op == 2:
                print("Perimeter of Circle:", circle_perimeter(r))
            elif op == 3:
                break
            else:
                print("Invalid choice!")

    elif choice == 2:   # Rectangle
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        while True:
            print("\n--- Rectangle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Rectangle Menu")
            op = int(input("Enter your choice: "))
            if op == 1:
                print("Area of Rectangle:", rectangle_area(l, b))
            elif op == 2:
                print("Perimeter of Rectangle:", rectangle_perimeter(l, b))
            elif op == 3:
                break
            else:
                print("Invalid choice!")

    elif choice == 3:   # Square
        s = float(input("Enter side: "))
        while True:
            print("\n--- Square Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Square Menu")
            op = int(input("Enter your choice: "))
            if op == 1:
                print("Area of Square:", square_area(s))
            elif op == 2:
                print("Perimeter of Square:", square_perimeter(s))
            elif op == 3:
                break
            else:
                print("Invalid choice!")

    elif choice == 4:   # Exit program
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
