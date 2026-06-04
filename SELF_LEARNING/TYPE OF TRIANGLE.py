angle1 = int(input("--Enter the first angle of the triangle: "))
if angle1 <= 0:
    print("-----Angle1 must be positive.-----")
    exit()

angle2 = int(input("--Enter the second angle of the triangle: "))
if angle2 <= 0:
    print("-----Angle2 must be positive.-----")
    exit()

angle3 = int(input("-- Enter the third angle of the triangle: "))
if angle3 <= 0:
    print("-----Angle3 must be positive.-----")
    exit()

if angle1 + angle2 + angle3 == 180:
    print("-----The angles form a triangle.-----",)

    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("-----It is a Right-Angled Triangle-----")

    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("-----It is an Acute-Angled Triangle----- ")

    else:
        print("-----It is an Obtuse-Angled Triangle-----")

else:
    print("-----The angles do not form a triangle.-----")


# python -u "CLASSWORK_PYTHON\SPECIFY TYPE OF TRIANGLE.py"