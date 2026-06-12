# Employee Performance Analyzer

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

def employees_above_80(performance):
    result = []
    for emp, score in performance.items():
        if score > 80:
            result.append(emp)
    return result

def count_needing_improvement(performance):
    count = 0
    for score in performance.values():
        if score < 60:
            count += 1
    return count

def top_performer(performance):
    max_emp = None
    max_score = -1
    for emp, score in performance.items():
        if score > max_score:
            max_emp = emp
            max_score = score
    return max_emp, max_score

def average_score(performance):
    total = 0
    for score in performance.values():
        total += score
    return total / len(performance)

def categorize(performance):
    excellent, good, average, poor = [], [], [], []
    for emp, score in performance.items():
        if score >= 90:
            excellent.append(emp)
        elif 75 <= score <= 89:
            good.append(emp)
        elif 60 <= score <= 74:
            average.append(emp)
        else:
            poor.append(emp)
    return excellent, good, average, poor

# ---- Driver Code ----
try:
    above_80 = employees_above_80(performance)
    improvement_count = count_needing_improvement(performance)
    top_emp, top_score = top_performer(performance)
    avg = average_score(performance)
    excellent, good, average, poor = categorize(performance)

    print("Employees Scoring Above 80:", " ".join(above_80))
    print("Employees Needing Improvement:", improvement_count)
    print(f"Top Performer: {top_emp} ({top_score})")
    print(f"Average Score: {avg:.1f}")
    print("Excellent:", excellent)
    print("Good:", good)
    print("Average:", average)
    print("Poor:", poor)

except Exception as e:
    print("Error occurred:", e)
