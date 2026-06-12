# City Temperature Monitoring System

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

# 1. Cities with temperature above 40°C
print("Cities Above 40°C:", end=" ")
for city in temperature:
    if temperature[city] > 40:
        print(city, end=" ")
print()

# 2. Hottest city
hottest_city = None
hottest_temp = -999
for city in temperature:
    if temperature[city] > hottest_temp:
        hottest_temp = temperature[city]
        hottest_city = city
print("Hottest City:", hottest_city, "(", hottest_temp, "°C)")

# 3. Coolest city
coolest_city = None
coolest_temp = 999
for city in temperature:
    if temperature[city] < coolest_temp:
        coolest_temp = temperature[city]
        coolest_city = city
print("Coolest City:", coolest_city, "(", coolest_temp, "°C)")

# 4. Average temperature
total = 0
for city in temperature:
    total += temperature[city]
average = total / len(temperature)
print("Average Temperature:", round(average, 1), "°C")

# 5. Pleasant cities (<35°C)
pleasant = []
for city in temperature:
    if temperature[city] < 35:
        pleasant.append(city)
print("Pleasant Cities:", pleasant)