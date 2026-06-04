# Mirror Number Check

num = input("Enter a number: ")
n = len(num)

# Step 1: Check even length (mirror possible only if split equally)
if n % 2 == 0:
    left_half = num[:n//2]
    right_half = num[n//2:]

    if left_half == right_half:
        print(num, "is a Mirror Number")
    else:
        print(num, "is NOT a Mirror Number")
else:
    print("Number must have even digits for mirror check")
