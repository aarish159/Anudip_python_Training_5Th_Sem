# Parking Slot Management System

parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# Display vacant parking slot numbers
def show_vacant(slots):
    print("Vacant Parking Slots:", end=" ")
    for i in range(len(slots)):
        if slots[i] == "Vacant":
            print(i+1, end=" ")
    print()

# Count occupied and vacant slots
def count_slots(slots):
    occupied = 0
    vacant = 0
    for s in slots:
        if s == "Occupied":
            occupied += 1
        else:
            vacant += 1
    print("Occupied Slots:", occupied, "Vacant Slots:", vacant)
    return occupied, vacant

# Allocate the first vacant slot
def allocate(slots):
    for i in range(len(slots)):
        if slots[i] == "Vacant":
            slots[i] = "Occupied"
            print(f"Vehicle Allocated to Slot {i+1}")
            return

# Calculate occupancy percentage
def occupancy(slots):
    occupied = 0
    total = 0
    for s in slots:
        total += 1
        if s == "Occupied":
            occupied += 1
    percent = (occupied / total) * 100
    print("Occupancy Percentage:", str(percent) + "%")

# Save updated parking info
def save(slots):
    f = open("parking.txt", "w")
    for i in range(len(slots)):
        f.write(f"Slot {i+1}: {slots[i]}\n")
    f.close()
    print("Parking Details Saved Successfully.")


# funtion call
show_vacant(parking_slots)
count_slots(parking_slots)
allocate(parking_slots)
occupancy(parking_slots)
save(parking_slots)
