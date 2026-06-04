# Strong Number check without math module and without function

num = int(input("Enter a number: "))
sum_val = 0
temp = num

while temp > 0:
    digit = temp % 10
    
    # factorial calculation directly
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    
    sum_val += fact
    temp //= 10

if sum_val == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")
