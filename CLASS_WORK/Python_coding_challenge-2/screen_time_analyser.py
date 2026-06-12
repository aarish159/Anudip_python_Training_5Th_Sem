# Mobile Screen Time Analyzer

screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]

# 1. Average screen time
total = 0
for t in screen_time:
    total += t
average = total / len(screen_time)
print("Average Screen Time:", round(average, 1), "minutes")

# 2. Highest and lowest screen time
highest = screen_time[0]
lowest = screen_time[0]
for t in screen_time:
    if t > highest:
        highest = t
    if t < lowest:
        lowest = t
print("Highest Screen Time:", highest, "minutes")
print("Lowest Screen Time:", lowest, "minutes")

# 3. Count days exceeding 200 minutes
count_exceed = 0
for t in screen_time:
    if t > 200:
        count_exceed += 1
print("Days Exceeding 200 Minutes:", count_exceed)

# 4. Display days with healthy usage (<180 minutes)
print("Healthy Usage Days:", end=" ")
for i in range(len(screen_time)):
    if screen_time[i] < 180:
        print("Day", i+1, end=" ")
print()

# 5. Categorize usage
healthy = 0
moderate = 0
excessive = 0
for t in screen_time:
    if t < 180:
        healthy += 1
    elif t <= 240:
        moderate += 1
    else:
        excessive += 1

print("Healthy:", healthy)
print("Moderate:", moderate)
print("Excessive:", excessive)
