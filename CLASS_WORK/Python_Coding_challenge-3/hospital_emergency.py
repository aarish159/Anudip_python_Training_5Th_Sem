# Problem: Emergency Ward Patient Analyzer

patients = [
    ("P101", "Critical"), ("P102", "Stable"), ("P103", "Critical"),
    ("P104", "Moderate"), ("P105", "Stable"), ("P106", "Critical"),
    ("P107", "Moderate"), ("P108", "Stable"), ("P109", "Critical"),
    ("P110", "Moderate")
]

def count_categories(patients):
    counts = {"Critical": 0, "Moderate": 0, "Stable": 0}
    for _, status in patients:
        counts[status] += 1
    return counts

def critical_patients(patients):
    return [pid for pid, status in patients if status == "Critical"]

def separate_lists(patients):
    critical, moderate, stable = [], [], []
    for pid, status in patients:
        if status == "Critical":
            critical.append(pid)
        elif status == "Moderate":
            moderate.append(pid)
        else:
            stable.append(pid)
    return critical, moderate, stable

def max_attention(counts):
    return max(counts, key=counts.get)

def save_critical(critical_list):
    with open("critical_patients.txt", "w") as f:
        for pid in critical_list:
            f.write(pid + "\n")

# ---- Driver Code ----
try:
    counts = count_categories(patients)
    critical_list = critical_patients(patients)
    critical, moderate, stable = separate_lists(patients)
    attention = max_attention(counts)
    save_critical(critical_list)

    print("Patient Count by Category:")
    for cat, val in counts.items():
        print(f"{cat} : {val}")

    print("Critical Patients:", " ".join(critical_list))
    print("Critical Patients List:", critical)
    print("Moderate Patients List:", moderate)
    print("Stable Patients List:", stable)
    print("Category Requiring Maximum Attention:", attention)
    print("Critical Patient Report Generated Successfully.")

except Exception as e:
    print("Error occurred:", e)
