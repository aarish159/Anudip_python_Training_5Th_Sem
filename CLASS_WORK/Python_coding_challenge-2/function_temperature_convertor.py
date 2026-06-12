# Function-Based Temperature Converter

temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]

# 1. Convert Celsius to Fahrenheit
def c_to_f(celsius):
    return (celsius * 9/5) + 32

# 2. Display all temperatures in Fahrenheit
fahrenheit_list = []
for t in temperatures:
    fahrenheit_list.append(c_to_f(t))

print("Temperatures in Fahrenheit:", end=" ")
for f in fahrenheit_list:
    print(round(f, 1), end=" ")
print()

# 3. Find the highest Fahrenheit temperature
highest = fahrenheit_list[0]
for f in fahrenheit_list:
    if f > highest:
        highest = f
print("Highest Temperature:", round(highest, 1), "°F")

# 4. Find the lowest Fahrenheit temperature
lowest = fahrenheit_list[0]
for f in fahrenheit_list:
    if f < lowest:
        lowest = f
print("Lowest Temperature:", round(lowest, 1), "°F")

# 5. Calculate the average Fahrenheit temperature
total = 0
for f in fahrenheit_list:
    total += f
average = total / len(fahrenheit_list)
print("Average Temperature:", round(average, 2), "°F")
