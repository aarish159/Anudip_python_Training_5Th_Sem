# Hospital Patient Monitoring System

heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

# 1. Display critical patients (heart rate >100)
print("Critical Patients:", end=" ")
for patient in heart_rate:
    if heart_rate[patient] > 100:
        print(patient, end=" ")
print()

# 2. Find highest and lowest heart rate
highest_patient = None
highest_rate = -999
lowest_patient = None
lowest_rate = 9999

for patient in heart_rate:
    if heart_rate[patient] > highest_rate:
        highest_rate = heart_rate[patient]
        highest_patient = patient
    if heart_rate[patient] < lowest_rate:
        lowest_rate = heart_rate[patient]
        lowest_patient = patient

print("Highest Heart Rate:", highest_patient, "(", highest_rate, "bpm)")
print("Lowest Heart Rate:", lowest_patient, "(", lowest_rate, "bpm)")

# 3. Calculate average heart rate
total = 0
for patient in heart_rate:
    total += heart_rate[patient]
average = total / len(heart_rate)
print("Average Heart Rate:", round(average, 1), "bpm")

# 4. Count stable patients (60–100 bpm)
stable_count = 0
for patient in heart_rate:
    if 60 <= heart_rate[patient] <= 100:
        stable_count += 1
print("Stable Patients:", stable_count)
