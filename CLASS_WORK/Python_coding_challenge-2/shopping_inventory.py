# Online Shopping Inventory System (Simple Version)

inventory = {
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

# 1. Products with stock below 15 units
print("Products with Stock Below 15:")
for product in inventory:
    if inventory[product] < 15:
        print(product)

# 2. Product with maximum stock
max_product = None
max_stock = -1
for product in inventory:
    if inventory[product] > max_stock:
        max_stock = inventory[product]
        max_product = product
print("Highest Stock Product:", max_product, "(", max_stock, "units)")

# 3. Product with minimum stock
min_product = None
min_stock = 9999
for product in inventory:
    if inventory[product] < min_stock:
        min_stock = inventory[product]
        min_product = product
print("Lowest Stock Product:", min_product, "(", min_stock, "units)")

# 4. Total stock available
total_stock = 0
for product in inventory:
    total_stock += inventory[product]
print("Total Stock Available:", total_stock)

# 5. Products requiring restocking (<10 units)
restock_list = []
for product in inventory:
    if inventory[product] < 10:
        restock_list.append(product)
print("Products Requiring Restocking:", restock_list)
