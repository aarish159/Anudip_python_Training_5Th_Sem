scores = [45, 78, 12, 100, 67, 8, 90, 55]

# 1. Count half-centuries (50–99) and centuries (100+)
half_centuries = 0
centuries = 0
for s in scores:
    if s >= 50 and s < 100:
        half_centuries += 1
    elif s >= 100:
        centuries += 1
print("Half-Centuries:", half_centuries)
print("Centuries:", centuries)

# 2. Find the highest score
highest = scores[0]
for s in scores:
    if s > highest:
        highest = s
print("\nHighest Score:", highest)

# 3. Display all scores below 20
print("\nScores below 20:")
for s in scores:
    if s < 20:
        print(s)

# 4. Calculate average score
total = 0
for s in scores:
    total += s
average = total / len(scores)
print("\nAverage Score:", average)
