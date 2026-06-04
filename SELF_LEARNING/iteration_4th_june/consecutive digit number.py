# Consecutive Number Check

num = int(input("Enter a number: "))
temp = num
prev_digit = temp % 10   # last digit
temp //= 10
flag = True

while temp > 0:
    curr_digit = temp % 10
    if prev_digit - curr_digit != 1:   # check difference
        flag = False
        break
    prev_digit = curr_digit
    temp //= 10

if flag:
    print(num, "is a Consecutive Number")
else:
    print(num, "is NOT a Consecutive Number")
