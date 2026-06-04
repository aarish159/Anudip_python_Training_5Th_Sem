# Water Tank Filling Program

# Initial values
water_level = 0
fill_rate = 10   # liters per minute
capacity = 100   # tank capacity in liters

# Loop until tank is full
while water_level < capacity:
    water_level += fill_rate
    print(f"Water Level: {water_level} liters")

print("Tank is full.")
