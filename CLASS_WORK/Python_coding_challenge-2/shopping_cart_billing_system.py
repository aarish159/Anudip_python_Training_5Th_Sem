# Shopping Cart Billing System

prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200)

# 1. Calculate total bill amount
total = 0
for p in prices:
    total += p
print("Total Bill Amount: ₹", total)

# 2. Find the most expensive product
max_price = prices[0]
for p in prices:
    if p > max_price:
        max_price = p
print("Most Expensive Product: ₹", max_price)

# 3. Find the least expensive product
min_price = prices[0]
for p in prices:
    if p < min_price:
        min_price = p
print("Least Expensive Product: ₹", min_price)

# 4. Count products costing more than ₹1000
count_more = 0
for p in prices:
    if p > 1000:
        count_more += 1
print("Products Costing More Than ₹1,000:", count_more)

# 5. Create a list of products eligible for discount (price > ₹800)
discount_list = []
for p in prices:
    if p > 800:
        discount_list.append(p)
print("Discount Eligible Products:", discount_list)
