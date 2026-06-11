# Ticket Booking System

tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}

# 1. Display available seats
def show_available(tickets):
    print("Available Seats:", end=" ")
    for seat in tickets:
        if tickets[seat] == "Available":
            print(seat, end=" ")
    print()

# 2. Count booked and available seats
def count_seats(tickets):
    booked = 0
    available = 0
    for seat in tickets:
        if tickets[seat] == "Booked":
            booked += 1
        else:
            available += 1
    print("Booked Seats:", booked, "Available Seats:", available)
    return booked, available

# 3. Reserve the first available seat
def reserve(tickets):
    for seat in tickets:
        if tickets[seat] == "Available":
            tickets[seat] = "Booked"
            print(f"Seat {seat} Reserved Successfully.")
            return

# 4. Save updated booking details
def save(tickets):
    f = open("tickets.txt", "w")
    for seat in tickets:
        f.write(f"{seat}: {tickets[seat]}\n")
    f.close()
    print("Booking Details Saved Successfully.")

# 5. Calculate hall occupancy percentage
def occupancy(tickets):
    booked = 0
    total = 0
    for seat in tickets:
        total += 1
        if tickets[seat] == "Booked":
            booked += 1
    percent = (booked / total) * 100
    print("Hall Occupancy Percentage:", str(percent) + "%")


# function calls
show_available(tickets)
count_seats(tickets)
reserve(tickets)
occupancy(tickets)
save(tickets)
