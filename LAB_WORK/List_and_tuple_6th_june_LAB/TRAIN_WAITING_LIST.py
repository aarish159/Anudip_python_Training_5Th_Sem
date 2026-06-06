passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# 1. Display all waiting-list passengers
print("Waiting List Passengers:")
for p in passengers:
    if p[1] == "Waiting":
        print(p[0])

# 2. Count confirmed and waiting passengers
confirmed = 0
waiting = 0
for p in passengers:
    if p[1] == "Confirmed":
        confirmed += 1
    else:
        waiting += 1
print("\nConfirmed:", confirmed)
print("Waiting:", waiting)

# 3. Find whether a specific passenger has a confirmed ticket
search_name = "Priya"
found = False
for p in passengers:
    if p[0] == search_name:
        if p[1] == "Confirmed":
            print("\n", search_name, "has a Confirmed ticket")
        else:
            print("\n", search_name, "is on Waiting list")
        found = True
        break
if not found:
    print("\nPassenger not found")

# 4. Create separate lists for confirmed and waiting passengers
confirmed_list = []
waiting_list = []
for p in passengers:
    if p[1] == "Confirmed":
        confirmed_list.append(p[0])
    else:
        waiting_list.append(p[0])

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)
