# Stock list
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# 1. Display products that are out of stock
out_of_stock = 0
for s in stock:
    if s == 0:
        out_of_stock += 1

# 2. Display products that need restocking (quantity < 10)
restock_required = []
for s in stock:
    if s < 10:
        restock_required.append(s)

# 3. Count available products (quantity > 0)
available_products = 0
for s in stock:
    if s > 0:
        available_products += 1

# 4. Create a new list containing only products with stock ≥ 15
healthy_stock = []
for s in stock:
    if s >= 15:
        healthy_stock.append(s)

# Output
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)
