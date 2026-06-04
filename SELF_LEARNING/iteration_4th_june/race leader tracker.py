# Lap Time Analysis

n = int(input("Enter number of racers: "))
lap_times = []

# Input lap times
for i in range(n):
    time = float(input(f"Enter lap time of racer {i+1}: "))
    lap_times.append(time)

# Find fastest and slowest
fastest_time = min(lap_times)
slowest_time = max(lap_times)

fastest_pos = lap_times.index(fastest_time) + 1
slowest_pos = lap_times.index(slowest_time) + 1

difference = slowest_time - fastest_time

# Display results
print("Fastest Racer Position:", fastest_pos)
print("Slowest Racer Position:", slowest_pos)
print("Difference:", difference)
