# Problem: Crop Moisture Analyzer

moisture = {
    "Field1": 55, "Field2": 30, "Field3": 72, "Field4": 28,
    "Field5": 64, "Field6": 35, "Field7": 80, "Field8": 42,
    "Field9": 25, "Field10": 68
}

def irrigation_required(moisture):
    result = []
    for field, level in moisture.items():
        if level < 40:
            result.append(field)
    return result

def categorize_fields(moisture):
    low, moderate, high = [], [], []
    for field, level in moisture.items():
        if level < 40:
            low.append(field)
        elif 40 <= level <= 69:
            moderate.append(field)
        else:
            high.append(field)
    return low, moderate, high

def count_categories(low, moderate, high):
    return len(low), len(moderate), len(high)

def highest_lowest(moisture):
    max_field, max_val = None, -1
    min_field, min_val = None, 101
    for field, level in moisture.items():
        if level > max_val:
            max_field, max_val = field, level
        if level < min_val:
            min_field, min_val = field, level
    return max_field, max_val, min_field, min_val

def irrigation_priority(moisture):
    # Sort fields needing irrigation by ascending moisture
    priority = sorted([f for f, v in moisture.items() if v < 40], key=lambda x: moisture[x])
    return priority

# ---- Driver Code ----
try:
    irrigation_fields = irrigation_required(moisture)
    low, moderate, high = categorize_fields(moisture)
    low_count, mod_count, high_count = count_categories(low, moderate, high)
    max_field, max_val, min_field, min_val = highest_lowest(moisture)
    priority_list = irrigation_priority(moisture)

    print("Fields Requiring Irrigation:", " ".join(irrigation_fields))
    print("Low Moisture Fields:", low)
    print("Moderate Moisture Fields:", moderate)
    print("High Moisture Fields:", high)
    print(f"Field with Highest Moisture: {max_field} ({max_val}%)")
    print(f"Field with Lowest Moisture: {min_field} ({min_val}%)")
    print("Irrigation Priority List:", priority_list)

except Exception as e:
    print("Error occurred:", e)
