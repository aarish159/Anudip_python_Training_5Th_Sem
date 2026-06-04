# Mountain Number Check

num = input("Enter a number: ")
n = len(num)

# Step 1: Find peak position (where increase stops)
i = 0
while i < n-1 and num[i] < num[i+1]:
    i += 1

# Step 2: After peak, digits must strictly decrease
while i < n-1 and num[i] > num[i+1]:
    i += 1

# Step 3: If we reached end, it's Mountain
if i == n-1 and n > 2:
    print(num, "is a Mountain Number")
else:
    print(num, "is NOT a Mountain Number")
