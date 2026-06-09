# Daily temperatures dictionary
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Cities having temperature above 40°C
print("Cities Above 40°C:", end=" ")
for city, temp in temperature.items():
    if temp > 40:
        print(city, end=" ")
print()

# 2. Hottest city
hottest_city = None
hottest_temp = -999
for city, temp in temperature.items():
    if temp > hottest_temp:
        hottest_temp = temp
        hottest_city = city
print("Hottest City:", hottest_city, "(", hottest_temp, "°C)")

# 3. Coolest city
coolest_city = None
coolest_temp = 999
for city, temp in temperature.items():
    if temp < coolest_temp:
        coolest_temp = temp
        coolest_city = city
print("Coolest City:", coolest_city, "(", coolest_temp, "°C)")

# 4. Average temperature
total = 0
for temp in temperature.values():
    total += temp
average = total / len(temperature)
print("Average Temperature:", round(average, 1), "°C")

# 5. Pleasant cities (temperature < 35°C)
pleasant = []
for city, temp in temperature.items():
    if temp < 35:
        pleasant.append(city)
print("Pleasant Cities:", pleasant)

# 6. Count cities with temperature between 35°C and 40°C
count = 0
for temp in temperature.values():
    if temp >= 35 and temp <= 40:
        count += 1
print("Cities Between 35°C and 40°C:", count)
