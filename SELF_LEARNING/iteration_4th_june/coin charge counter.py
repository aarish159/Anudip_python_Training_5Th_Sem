# Minimum Notes Calculator

amount = int(input("Enter amount: "))

notes = [500, 200, 100, 50, 20, 10]

print("Amount:", amount)

for note in notes:
    count = amount // note   # kitne notes banenge
    if count > 0:
        print(note, "x", count)
    amount = amount % note   # remaining amount
