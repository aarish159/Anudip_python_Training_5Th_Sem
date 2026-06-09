# Employee performance scores dictionary
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Employees scoring above 80
print("Employees Scoring Above 80:", end=" ")
for emp, score in performance.items():
    if score > 80:
        print(emp, end=" ")
print()

# 2. Count employees needing improvement (score < 60)
improvement_count = 0
for score in performance.values():
    if score < 60:
        improvement_count += 1
print("Employees Needing Improvement:", improvement_count)

# 3. Top performer
top_emp = None
top_score = -1
for emp, score in performance.items():
    if score > top_score:
        top_score = score
        top_emp = emp
print("Top Performer:", top_emp, "(", top_score, ")")

# 4. Average performance score
total = 0
for score in performance.values():
    total += score
average = total / len(performance)
print("Average Score:", round(average, 1))

# 5. Categorize employees
excellent = []
good = []
average_list = []
poor = []

for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average_list.append(emp)
    else:
        poor.append(emp)

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average_list)
print("Poor:", poor)
