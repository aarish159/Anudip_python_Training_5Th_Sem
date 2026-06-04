# Secret Code Validation

code = input("Enter 6-digit code: ")

# Step 1: Check length
if len(code) == 6 and code.isdigit():
    first_sum = int(code[0]) + int(code[1]) + int(code[2])
    last_sum  = int(code[3]) + int(code[4]) + int(code[5])

    if first_sum == last_sum:
        print(code, "is a Valid Code")
    else:
        print(code, "is an Invalid Code")
else:
    print("Code must contain exactly 6 digits")
