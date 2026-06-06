bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Confirmed passengers
print("Confirmed Passengers:")
for passenger in bookings:
    if passenger[2] == "Confirmed":
        print(passenger[0], passenger[1])

# 2. Count passengers to Delhi
delhi_count = 0
for passenger in bookings:
    if passenger[1] == "Delhi":
        delhi_count += 1
print("\nPassengers Travelling to Delhi:", delhi_count)

# 3. Count each status
confirmed_count = 0
waiting_count = 0
cancelled_count = 0
for passenger in bookings:
    if passenger[2] == "Confirmed":
        confirmed_count += 1
    elif passenger[2] == "Waiting":
        waiting_count += 1
    elif passenger[2] == "Cancelled":
        cancelled_count += 1
print("\nConfirmed:", confirmed_count, "Waiting:", waiting_count, "Cancelled:", cancelled_count)

# 4. Waiting list IDs
waiting_list = []
for passenger in bookings:
    if passenger[2] == "Waiting":
        waiting_list.append(passenger[0])
print("\nWaiting List:", waiting_list)

# 5. Most booked destination
destination_count = {}
for passenger in bookings:
    destination = passenger[1]
    if destination in destination_count:
        destination_count[destination] += 1
    else:
        destination_count[destination] = 1

most_booked = max(destination_count, key=destination_count.get)
print("\nMost Booked Destination:", most_booked)
