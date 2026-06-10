#module name is geometry.py
pi=3.14

#for circle
def circle_area(radius):
    return pi*radius*radius
def circle_parameter(radius):
    return 2*pi*radius

# for square
def square_area(side):
    return side*side
def square_parameter(side):
    return 4*side

#for rectangle
def rectangle_area(length,width):
    return length*width
def rectangle_paramater(length,width):
    return 2*(length*width)
 