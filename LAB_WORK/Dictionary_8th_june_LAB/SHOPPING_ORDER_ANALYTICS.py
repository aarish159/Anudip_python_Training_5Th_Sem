# Sales data dictionary
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Products sold more than 20 times
print("Products Sold More Than 20 Times:", end=" ")
for product, qty in sales.items():
    if qty > 20:
        print(product, end=" ")
print()

# 2. Best-selling product
best_product = None
best_sales = -1
for product, qty in sales.items():
    if qty > best_sales:
        best_sales = qty
        best_product = product
print("Best Selling Product:", best_product, "(", best_sales, ")")

# 3. Least-selling product
least_product = None
least_sales = 999999
for product, qty in sales.items():
    if qty < least_sales:
        least_sales = qty
        least_product = product
print("Least Selling Product:", least_product, "(", least_sales, ")")

# 4. Total products sold
total = 0
for qty in sales.values():
    total += qty
print("Total Units Sold:", total)

# 5. Products requiring promotion (sales < 15)
promotion_list = []
for product, qty in sales.items():
    if qty < 15:
        promotion_list.append(product)
print("Products Requiring Promotion:", promotion_list)

# 6. Count products having sales between 10 and 30
count = 0
for qty in sales.values():
    if qty >= 10 and qty <= 30:
        count += 1
print("Products Having Sales Between 10 and 30:", count)
