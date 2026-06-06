slots = [1, 0, 1, 1, 0, 0, 1, 0]

# 1. Count occupied and available slots
occupied = 0
available = 0
for s in slots:
    if s == 1:
        occupied += 1
    else:
        available += 1
print("Occupied Slots:", occupied)
print("Available Slots:", available)

# 2. Find the first available slot
first_available = None
for i in range(len(slots)):
    if slots[i] == 0:
        first_available = i + 1   # slot number = index+1
        break
print("\nFirst Available Slot:", first_available)

# 3. Display all available slot numbers
available_slots = []
for i in range(len(slots)):
    if slots[i] == 0:
        available_slots.append(i + 1)
print("\nAvailable Slot Numbers:", available_slots)

# 4. Check whether parking occupancy exceeds 75%
total_slots = len(slots)
occupancy = (occupied / total_slots) * 100
if occupancy > 75:
    status = "Occupancy exceeds 75%"
else:
    status = "Occupancy does not exceed 75%"
print("\nParking Occupancy:", str(int(occupancy)) + "%")
print("Status:", status)
