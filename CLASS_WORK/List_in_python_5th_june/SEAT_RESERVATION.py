# Seats list
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# 1. Count booked and available seats
booked = 0
available = 0
for s in seats:
    if s == 1:
        booked += 1
    else:
        available += 1

# 2. Find the first available seat (index + 1 for seat number)
first_available = None
for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1
        break

# 3. Create a list of all available seat numbers
available_seats = []
for i in range(len(seats)):
    if seats[i] == 0:
        available_seats.append(i + 1)

# 4. Determine bus occupancy percentage
total_seats = len(seats)
occupancy = (booked / total_seats) * 100
status = "More Than 70% Occupied" if occupancy > 70 else "Not More Than 70% Occupied"

# Output
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)
print("Bus Occupancy:", str(int(occupancy)) + "%")
print("Status:", status)
