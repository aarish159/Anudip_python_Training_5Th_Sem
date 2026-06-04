num = int(input("Enter a number: "))
reverse = 0
temp = num

# Reverse calculation
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse:", reverse)

# Palindrome check
if reverse == num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
