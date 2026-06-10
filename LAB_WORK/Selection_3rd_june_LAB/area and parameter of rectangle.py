print("------ Area and Perimeter of Rectangle ------")

length = float(input("ENTER LENGTH: "))
breadth = float(input("ENTER BREADTH: "))

if length > 0 and breadth > 0:
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area =", area)
    print("Perimeter =", perimeter)
else:
    print("Invalid Data! Length and Breadth must be positive.")