# Passenger booking records stored in a tuple
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display all passengers with Confirmed status
print("Confirmed Passengers:")
for passenger in bookings:
    if passenger[2] == "Confirmed":
        print(passenger[0], passenger[1])

# 2. Count passengers travelling to Delhi
delhi_count = sum(1 for passenger in bookings if passenger[1] == "Delhi")
print("\nPassengers Travelling to Delhi:", delhi_count)

# 3. Count Confirmed, Waiting, and Cancelled bookings separately
confirmed_count = sum(1 for passenger in bookings if passenger[2] == "Confirmed")
waiting_count = sum(1 for passenger in bookings if passenger[2] == "Waiting")
cancelled_count = sum(1 for passenger in bookings if passenger[2] == "Cancelled")
print("\nConfirmed:", confirmed_count, "Waiting:", waiting_count, "Cancelled:", cancelled_count)

# 4. Create list of passenger IDs with Waiting status
waiting_list = [passenger[0] for passenger in bookings if passenger[2] == "Waiting"]
print("\nWaiting List:", waiting_list)

# 5. Determine destination with highest number of bookings
destination_count = {}
for passenger in bookings:
    destination = passenger[1]
    destination_count[destination] = destination_count.get(destination, 0) + 1

most_booked = max(destination_count, key=destination_count.get)
print("\nMost Booked Destination:", most_booked)
