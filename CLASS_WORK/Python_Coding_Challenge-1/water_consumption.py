# Monthly Water Consumption Analysis

water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

# 1. Display houses consuming more than 3000 litres
def high_consumers(data):
    print("Houses Consuming More Than 3000 Litres:", end=" ")
    for house in data:
        if data[house] > 3000:
            print(house, end=" ")
    print()

# 2. Find highest and lowest consumers
def extremes(data):
    highest_house = ""
    lowest_house = ""
    highest = -1
    lowest = 999999

    for house in data:
        usage = data[house]
        if usage > highest:
            highest = usage
            highest_house = house
        if usage < lowest:
            lowest = usage
            lowest_house = house

    print(f"Highest Consumption: {highest_house} ({highest} litres)")
    print(f"Lowest Consumption: {lowest_house} ({lowest} litres)")
    return highest, lowest

# 3. Calculate total water consumption
def total_consumption(data):
    total = 0
    for house in data:
        total += data[house]
    print("Total Consumption:", str(total) + " litres")
    return total

# 4. Categorize houses
def categorize(data):
    low = []
    medium = []
    high = []
    for house in data:
        usage = data[house]
        if usage < 2000:
            low.append(house)
        elif usage <= 3500:
            medium.append(house)
        else:
            high.append(house)
    print("Low Consumption:", low)
    print("Medium Consumption:", medium)
    print("High Consumption:", high)
    return low, medium, high

# 5. Count households eligible for conservation awareness (>2500 litres)
def eligible(data):
    count = 0
    for house in data:
        if data[house] > 2500:
            count += 1
    print("Eligible Households:", count)


# function calls
high_consumers(water_usage)
extremes(water_usage)
total_consumption(water_usage)
categorize(water_usage)
eligible(water_usage)
