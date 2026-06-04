# Electricity Bill Calculator with Surcharge

units = int(input("Enter units consumed: "))
bill = 0

# Slab calculation
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# Surcharge check
if bill > 5000:
    surcharge = bill * 0.10
    bill += surcharge
else:
    surcharge = 0

# Display
print("Units Consumed:", units)
print("Base Bill: ₹", bill - surcharge)
print("Surcharge: ₹", surcharge)
print("Final Payable Amount: ₹", bill)
