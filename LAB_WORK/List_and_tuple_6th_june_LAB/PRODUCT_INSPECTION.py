products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# 1. Display failed product IDs
print("Failed Product IDs:")
for p in products:
    if p[1] == "Fail":
        print(p[0])

# 2. Count passed and failed products
passed = 0
failed = 0
for p in products:
    if p[1] == "Pass":
        passed += 1
    else:
        failed += 1
print("\nPassed:", passed)
print("Failed:", failed)

# 3. Calculate pass percentage
total = len(products)
pass_percentage = (passed / total) * 100
print("\nPass Percentage:", pass_percentage, "%")

# 4. Stop checking if 3 failures are found
fail_count = 0
print("\nChecking with stop condition:")
for p in products:
    if p[1] == "Fail":
        print("Failure found at Product ID:", p[0])
        fail_count += 1
        if fail_count == 3:
            print("Stopped checking after 3 failures.")
            break
