passengers = [12, 18, 25, 30, 28, 15, 8]

# 1. Find the busiest stop
busiest = passengers[0]
busiest_pos = 1
for i in range(len(passengers)):
    if passengers[i] > busiest:
        busiest = passengers[i]
        busiest_pos = i + 1
print("Busiest Stop:", busiest_pos, "with", busiest, "passengers")

# 2. Display stops with fewer than 10 passengers
print("\nStops with fewer than 10 passengers:")
for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1, "-", passengers[i])

# 3. Calculate average passengers
total = 0
for p in passengers:
    total += p
average = total / len(passengers)
print("\nAverage Passengers:", average)

# 4. Determine whether any stop exceeded 25 passengers
exceeded = False
for p in passengers:
    if p > 25:
        exceeded = True
        break

if exceeded:
    print("\nYes, at least one stop exceeded 25 passengers")
else:
    print("\nNo stop exceeded 25 passengers")
