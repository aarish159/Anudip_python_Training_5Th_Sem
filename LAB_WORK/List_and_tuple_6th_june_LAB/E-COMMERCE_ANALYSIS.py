orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# 1. Display products costing more than ₹1000
print("Products costing more than ₹1000:")
for item in orders:
    if item[1] > 1000:
        print(item[0], item[1])

# 2. Find the most expensive product
most_expensive = orders[0]   # assume first product
for item in orders:
    if item[1] > most_expensive[1]:
        most_expensive = item
print("\nMost Expensive Product:", most_expensive[0], most_expensive[1])

# 3. Calculate total order value
total_value = 0
for item in orders:
    total_value += item[1]
print("\nTotal Order Value: ₹", total_value)

# 4. Count products costing below ₹1000
below_1000 = 0
for item in orders:
    if item[1] < 1000:
        below_1000 += 1
print("\nProducts costing below ₹1000:", below_1000)
