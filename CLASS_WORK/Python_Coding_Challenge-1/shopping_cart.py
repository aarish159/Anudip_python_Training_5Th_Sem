# Shopping Cart Management System

cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

#  Calculate total cart value
def total_value(cart):
    total = 0
    for price in cart:
        total += price
    print("Total Cart Value: ₹", total)
    return total

#  Find most expensive and cheapest products
def find_extremes(cart):
    max_price = cart[0]
    min_price = cart[0]
    for price in cart:
        if price > max_price:
            max_price = price
        if price < min_price:
            min_price = price
    print("Most Expensive Product: ₹", max_price)
    print("Cheapest Product: ₹", min_price)
    return max_price, min_price

#  Count premium shipping products (price > 1000)
def premium_shipping(cart):
    count = 0
    for price in cart:
        if price > 1000:
            count += 1
    print("Premium Shipping Eligible Products:", count)
    return count

#  Generate discount list (products above 1500)
def discount_list(cart):
    discount = []
    for price in cart:
        if price > 1500:
            discount.append(price)
    print("Discount Eligible Products:", discount)
    return discount

#  Calculate average product price
def average_price(cart):
    total = 0
    count = 0
    for price in cart:
        total += price
        count += 1
    avg = total / count
    print("Average Product Price: ₹", avg)


# function call
total_value(cart)
find_extremes(cart)
premium_shipping(cart)
discount_list(cart)
average_price(cart)
