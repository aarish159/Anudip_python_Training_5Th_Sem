# Seats list
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# 1. Count booked and available seats
def count_seats(seats):
    booked = 0
    available = 0
    for s in seats:
        if s == "Booked":
            booked += 1
        else:
            available += 1
    return booked, available

# 2. First available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1   # seat number (1-based)
    return -1   # if none available

# 3. Occupancy percentage
def occupancy_percentage(seats):
    booked, available = count_seats(seats)
    total = len(seats)
    return (booked / total) * 100

# 4. Display all available seat numbers
def display_available_seats(seats):
    available_seats = []
    for i in range(len(seats)):
        if seats[i] == "Available":
            available_seats.append(i + 1)
    return available_seats


# ---- Main Execution ----
booked, available = count_seats(seats)
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available(seats))
print("Occupancy Percentage:", round(occupancy_percentage(seats), 2), "%")
print("Available Seat Numbers:", *display_available_seats(seats))
