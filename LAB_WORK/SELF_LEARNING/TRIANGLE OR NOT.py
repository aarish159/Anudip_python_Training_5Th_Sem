a = int(input("Enter first angle: "))       
if a <= 0: 
    print("Invalid input. Angle must be greater than 0.")
    exit()
b = int(input("Enter second angle: ")) 
if b <= 0:
    print("Invalid input. Angle must be greater than 0.")
    exit()      
c = int(input("Enter third angle: "))
if c <= 0:                          
    print("Invalid input. Angle must be greater than 0.")
    exit()          
if a + b + c == 180:
    print("The angles form a triangle.")            
else:   print("The angles do not form a triangle.") 