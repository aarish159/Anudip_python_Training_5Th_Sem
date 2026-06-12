# Monthly Electricity Consumption Analysis

#given data
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

#displaying houses consuming more than 400 units
def houses_more_than_400(units):
    result=[]
    for h in units:
        if units[h] > 400:
            result.append(h)
    return result

#highest consuming house
def highest_house(untis):
    houses=list(units.keys())
    highest=houses[0]
    for h in houses:
        if units[h]>units[highest]:
            highest = h
    return highest,units[highest]

#finding lowest consuming house
def lowest_house(units):
    houses=list(units.keys())
    lowest=houses[0]
    for h in units:
        if units[h]< units[lowest]:
            lowest =h
    return lowest, units[lowest]

# calculate total units
def total_units(units):
    total = 0
    for h in units:
        total += units[h]
    return total

# categorize houses
def categorize(units):
    low, medium, high = [], [], []
    for h in units:
        u = units[h]
        if u < 200:
            low.append(h)
        elif u <= 400:
            medium.append(h)
        else:
            high.append(h)
    return low, medium, high

# count eligible houses (>300 units)
def eligible_count(units):
    count = 0
    for h in units:
        if units[h] > 300:
            count += 1
    return count

# dunction call
high_consumers = houses_more_than_400(units)
highest = highest_house(units)
lowest = lowest_house(units)
total = total_units(units)
low, medium, high = categorize(units)
eligible = eligible_count(units)

# --- Output ---
print("Houses Consuming More Than 400 Units:", " ".join(high_consumers))
print("Highest Consumption:", highest[0], "(", highest[1], "units)")
print("Lowest Consumption:", lowest[0], "(", lowest[1], "units)")
print("Total Units Consumed:", total)
print("Low Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)
print("Eligible for Energy-Saving Campaign:", eligible)