# Runs Scored by Players in a Tournament

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

# 1. Orange Cap Winner (highest runs)
max_player = None
max_runs = -1
for player in runs:
    if runs[player] > max_runs:
        max_runs = runs[player]
        max_player = player
print("Orange Cap Winner:", max_player, "(", max_runs, "runs)")

# 2. Lowest Scorer
min_player = None
min_runs = 9999
for player in runs:
    if runs[player] < min_runs:
        min_runs = runs[player]
        min_player = player
print("Lowest Scorer:", min_player, "(", min_runs, "runs)")

# 3. Total Runs Scored
total = 0
for player in runs:
    total += runs[player]
print("Total Runs:", total)

# 4. Players scoring more than 500 runs
print("Players Scoring Above 500:", end=" ")
for player in runs:
    if runs[player] > 500:
        print(player, end=" ")
print()

# 5. Players scoring below 400
below_400 = []
for player in runs:
    if runs[player] < 400:
        below_400.append(player)
print("Players Scoring Below 400:", below_400)
