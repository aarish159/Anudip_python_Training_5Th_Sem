# creating module for area and parameter as area_parameter.py
pi=3.14

#for rectangle
def rectangle_area(length,breath):
    return length*breath
def rectangle_parameter(length,breath):
    return 2*(length*breath)

#for square
def square_are(side):
    return side*side
def square_parameter(side):
    return 4*side

#for circle
def circle_area(radius):
    return pi*radius*radius
def circle_parameter(radius):
    return 2*pi*radius