attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# 1. Count present and absent days
present = 0
absent = 0
for day in attendance:
    if day == 'P':
        present += 1
    else:
        absent += 1
print("Present Days:", present)
print("Absent Days:", absent)

# 2. Calculate attendance percentage
total_days = len(attendance)
percentage = (present / total_days) * 100
print("\nAttendance Percentage:", percentage, "%")

# 3. Determine eligibility (minimum 75%)
if percentage >= 75:
    print("Eligibility: Eligible")
else:
    print("Eligibility: Not Eligible")

# 4. Display positions where student was absent
print("\nAbsent on Days (positions):")
for i in range(len(attendance)):
    if attendance[i] == 'A':
        print("Day", i + 1)
