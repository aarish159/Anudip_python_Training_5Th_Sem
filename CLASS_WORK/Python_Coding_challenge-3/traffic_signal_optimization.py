# Problem: Traffic Condition Analyzer

traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85]

def classify_traffic(traffic):
    conditions = []
    for count in traffic:
        if count < 80:
            conditions.append((count, "Low"))
        elif 80 <= count <= 150:
            conditions.append((count, "Moderate"))
        else:
            conditions.append((count, "High"))
    return conditions

def count_conditions(conditions):
    low = sum(1 for _, c in conditions if c == "Low")
    moderate = sum(1 for _, c in conditions if c == "Moderate")
    high = sum(1 for _, c in conditions if c == "High")
    return low, moderate, high

def peak_traffic(traffic):
    max_val = traffic[0]
    for t in traffic:
        if t > max_val:
            max_val = t
    return max_val

def separate_lists(conditions):
    low_list, mod_list, high_list = [], [], []
    for val, c in conditions:
        if c == "Low":
            low_list.append(val)
        elif c == "Moderate":
            mod_list.append(val)
        else:
            high_list.append(val)
    return low_list, mod_list, high_list

def manual_control_required(high_count):
    return "Yes" if high_count > 3 else "No"

# ---- Driver Code ----
try:
    conditions = classify_traffic(traffic)
    for val, c in conditions:
        print(f"{val} → {c}")

    low_count, mod_count, high_count = count_conditions(conditions)
    peak = peak_traffic(traffic)
    low_list, mod_list, high_list = separate_lists(conditions)
    control = manual_control_required(high_count)

    print("\nLow Traffic Intervals:", low_count)
    print("Moderate Traffic Intervals:", mod_count)
    print("High Traffic Intervals:", high_count)
    print(f"Peak Traffic Count: {peak} vehicles")
    print("Low Traffic List:", low_list)
    print("Moderate Traffic List:", mod_list)
    print("High Traffic List:", high_list)
    print("Manual Traffic Control Required:", control)

except Exception as e:
    print("Error occurred:", e)
