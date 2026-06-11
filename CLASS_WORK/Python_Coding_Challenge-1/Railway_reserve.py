#Given data
seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}

# 1. Display all available seats
def show_available(seats):
    print("Available Seats:", end=" ")
    for seat in seats:
        if seats[seat] == "Available":
            print(seat, end=" ")
    print()

# Count booked and available seats
def count_seats(seats):
    booked = 0
    available = 0
    for seat in seats:
        if seats[seat] == "Booked":
            booked += 1
        else:
            available += 1
    print("Booked Seats:", booked, "Available Seats:", available)
    return booked, available

# Reserve first available seat
def reserve(seats):
    for seat in seats:
        if seats[seat] == "Available":
            seats[seat] = "Booked"
            print(f"Seat {seat} Reserved Successfully.")
            return

# Save reservations
def save(seats):
    f = open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_Coding_Challenge-1\reservations.txt", "w")
    for seat in seats:
        f.write(f"Seat {seat}: {seats[seat]}\n")
    f.close()
    print("Reservation Details Saved Successfully.")

#  Occupancy percentage
def occupancy(seats):
    booked = 0
    total = 0
    for seat in seats:
        total += 1
        if seats[seat] == "Booked":
            booked += 1
    percent = (booked / total) * 100
    print("Occupancy Percentage:", str(percent) + "%")


# function call
show_available(seats)
booked, available = count_seats(seats)
reserve(seats)
occupancy(seats)
save(seats)