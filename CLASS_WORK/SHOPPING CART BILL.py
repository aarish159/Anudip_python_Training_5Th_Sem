# Shopping Cart Billing Program

total_bill = 0

while True:
    price = float(input("Enter Item Price: "))
    
    if price == 0:   # Stop when user enters 0
        break
    
    total_bill += price
print(f"\nTotal Bill Amount: ₹{total_bill}")