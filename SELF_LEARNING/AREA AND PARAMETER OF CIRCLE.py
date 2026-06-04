print("------ Area and Perimeter of Circle ------")
radius = float(input("ENTER RADIUS: "))
if radius > 0:
    area = 3.14 * radius * radius
    perimeter = 2 * 3.14 * radius
    print("Area =", area)
    print("Perimeter =", perimeter)
else:
    print("Invalid Data! Radius must be positive.")