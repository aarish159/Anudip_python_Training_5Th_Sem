# Monthly electricity consumption dictionary
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:", end=" ")
for house, unit in units.items():
    if unit > 400:
        print(house, end=" ")
print()

# 2. Highest-consuming house
highest_house = None
highest_units = -1
for house, unit in units.items():
    if unit > highest_units:
        highest_units = unit
        highest_house = house
print("Highest Consumption:", highest_house, "(", highest_units, "units)")

# 3. Lowest-consuming house
lowest_house = None
lowest_units = 999999
for house, unit in units.items():
    if unit < lowest_units:
        lowest_units = unit
        lowest_house = house
print("Lowest Consumption:", lowest_house, "(", lowest_units, "units)")

# 4. Total units consumed
total = 0
for unit in units.values():
    total += unit
print("Total Units Consumed:", total)

# 5. Categorize houses
low = []
medium = []
high = []

for house, unit in units.items():
    if unit < 200:
        low.append(house)
    elif unit <= 400:
        medium.append(house)
    else:
        high.append(house)

print("Low Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)

# 6. Count houses eligible for energy-saving campaign (>300 units)
eligible_count = 0
for unit in units.values():
    if unit > 300:
        eligible_count += 1
print("Eligible for Energy-Saving Campaign:", eligible_count)
