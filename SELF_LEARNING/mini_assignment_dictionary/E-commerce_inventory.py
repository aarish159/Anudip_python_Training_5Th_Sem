# E-Commerce Inventory & Sales Dashboard

products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Mouse", "price": 800, "stock": 50, "sold": 45},
    "P103": {"name": "Keyboard", "price": 1500, "stock": 20, "sold": 32},
    "P104": {"name": "Monitor", "price": 12000, "stock": 5, "sold": 12},
    "P105": {"name": "Headphones", "price": 2000, "stock": 8, "sold": 28},
    "P106": {"name": "Printer", "price": 7000, "stock": 2, "sold": 8},
    "P107": {"name": "Webcam", "price": 1500, "stock": 10, "sold": 20},
    "P108": {"name": "Speaker", "price": 2500, "stock": 4, "sold": 18},
    "P109": {"name": "Tablet", "price": 30000, "stock": 6, "sold": 10},
    "P110": {"name": "Router", "price": 3500, "stock": 15, "sold": 25},
    "P111": {"name": "SSD", "price": 6000, "stock": 3, "sold": 14},
    "P112": {"name": "HDD", "price": 4000, "stock": 7, "sold": 9},
    "P113": {"name": "Smartphone", "price": 25000, "stock": 9, "sold": 30},
    "P114": {"name": "Charger", "price": 500, "stock": 40, "sold": 35},
    "P115": {"name": "Power Bank", "price": 1500, "stock": 12, "sold": 22},
    "P116": {"name": "Camera", "price": 45000, "stock": 5, "sold": 11},
    "P117": {"name": "Tripod", "price": 1200, "stock": 6, "sold": 13},
    "P118": {"name": "Mic", "price": 1800, "stock": 8, "sold": 15},
    "P119": {"name": "Projector", "price": 30000, "stock": 2, "sold": 7},
    "P120": {"name": "Smartwatch", "price": 12000, "stock": 10, "sold": 19},
    "P121": {"name": "VR Headset", "price": 20000, "stock": 3, "sold": 6},
    "P122": {"name": "Drone", "price": 60000, "stock": 1, "sold": 5},
    "P123": {"name": "Gaming Console", "price": 40000, "stock": 4, "sold": 9},
    "P124": {"name": "Graphics Card", "price": 35000, "stock": 2, "sold": 12},
    "P125": {"name": "RAM", "price": 2500, "stock": 20, "sold": 27},
    "P126": {"name": "Motherboard", "price": 15000, "stock": 3, "sold": 8},
    "P127": {"name": "CPU", "price": 30000, "stock": 2, "sold": 10},
    "P128": {"name": "UPS", "price": 5000, "stock": 6, "sold": 14},
    "P129": {"name": "Scanner", "price": 8000, "stock": 2, "sold": 6},
    "P130": {"name": "TV", "price": 55000, "stock": 5, "sold": 16}
}

# 1. Display all products
def display_all(products):
    for pid, info in products.items():
        print(pid, "->", info)

# 2. Add new product
def add_product(products, pid, name, price, stock, sold):
    products[pid] = {"name": name, "price": price, "stock": stock, "sold": sold}

# 3. Update stock after sales
def update_stock(products, pid, qty_sold):
    if pid in products:
        products[pid]["stock"] -= qty_sold
        products[pid]["sold"] += qty_sold

# 4. Out-of-stock products
def out_of_stock(products):
    return [info["name"] for info in products.values() if info["stock"] == 0]

# 5. Stock less than 5
def low_stock(products):
    return [info["name"] for info in products.values() if info["stock"] < 5]

# 6. Total inventory value
def inventory_value(products):
    return sum(info["price"] * info["stock"] for info in products.values())

# 7. Best-selling product
def best_selling(products):
    return max(products.items(), key=lambda x: x[1]["sold"])

# 8. Least-selling product
def least_selling(products):
    return min(products.items(), key=lambda x: x[1]["sold"])

# 9. Total revenue
def total_revenue(products):
    return sum(info["price"] * info["sold"] for info in products.values())

# 10. Low-stock report
def low_stock_report(products):
    return {pid: info for pid, info in products.items() if info["stock"] < 5}

# 11. Sales above average
def sales_above_avg(products):
    avg = sum(info["sold"] for info in products.values()) / len(products)
    return [info["name"] for info in products.values() if info["sold"] > avg]

# 12. Promotion products (sales < 10)
def promotion_products(products):
    return {pid: info for pid, info in products.items() if info["sold"] < 10}

# Challenge: Business Report
def business_report(products):
    print("=== Business Report ===")
    print("Total Inventory Value: Rs", inventory_value(products))
    print("Total Revenue: Rs", total_revenue(products))
    print("Best Selling:", best_selling(products))
    print("Least Selling:", least_selling(products))
    print("Out of Stock:", out_of_stock(products))
    print("Low Stock:", low_stock(products))
    print("Sales Above Average:", sales_above_avg(products))
    print("Promotion Products:", promotion_products(products))
    print("=======================")


# ---- Main Execution ----
display_all(products)
business_report(products)