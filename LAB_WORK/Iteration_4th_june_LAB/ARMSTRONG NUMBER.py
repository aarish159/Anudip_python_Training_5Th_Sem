# Armstrong number check

num = int(input("Enter a number: "))
order = len(str(num))   # number of digits
sum_val = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp //= 10

if sum_val == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
