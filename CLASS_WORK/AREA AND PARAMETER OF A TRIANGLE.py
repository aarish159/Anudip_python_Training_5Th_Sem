side1=int(input("Enter the length of the first side of the triangle: "))
side2=int(input("Enter the length of the second side of the triangle: "))
side3=int(input("Enter the length of the third side of the triangle: "))
s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
print("The area of the triangle is: ", area)
perimeter=side1+side2+side3
print("The perimeter of the triangle is: ", perimeter)