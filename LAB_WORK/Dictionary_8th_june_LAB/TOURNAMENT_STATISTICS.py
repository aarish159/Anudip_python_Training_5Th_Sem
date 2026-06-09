# Runs scored by players
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:", end=" ")
for player, score in runs.items():
    if score > 500:
        print(player, end=" ")
print()

# 2. Orange Cap winner (highest scorer)
orange_cap = None
max_runs = -1
for player, score in runs.items():
    if score > max_runs:
        max_runs = score
        orange_cap = player
print("Orange Cap Winner:", orange_cap, "(", max_runs, ")")

# 3. Lowest scorer
lowest_player = None
lowest_runs = 999999
for player, score in runs.items():
    if score < lowest_runs:
        lowest_runs = score
        lowest_player = player
print("Lowest Scorer:", lowest_player, "(", lowest_runs, ")")

# 4. Total runs scored
total = 0
for score in runs.values():
    total += score
print("Total Tournament Runs:", total)

# 5. Players scoring below 400
below_400 = []
for player, score in runs.items():
    if score < 400:
        below_400.append(player)
print("Players Scoring Below 400:", below_400)

# 6. Count players scoring between 400 and 600
count = 0
for score in runs.values():
    if score >= 400 and score <= 600:
        count += 1
print("Players Between 400 and 600 Runs:", count)
