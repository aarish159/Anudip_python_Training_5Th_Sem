# Transaction Analysis

above_50000 = 0
below_1000 = 0
total_amount = 0

while True:
    amt = int(input("Enter transaction amount (-1 to stop): "))
    if amt == -1:
        break
    total_amount += amt
    if amt > 50000:
        above_50000 += 1
    if amt < 1000:
        below_1000 += 1

# Display results
print("Transactions above ₹50,000:", above_50000)
print("Transactions below ₹1,000:", below_1000)
print("Total Transaction Amount: ₹", total_amount)
