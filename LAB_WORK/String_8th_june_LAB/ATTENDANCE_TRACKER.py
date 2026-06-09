# Attendance record
attendance = "PPAPPPAAPPPPAPP"
print("Attendance Record:", attendance)

# 1. Count Present and Absent days
present = 0
absent = 0
for ch in attendance:
    if ch == 'P':
        present += 1
    else:
        absent += 1
print("Present Days:", present)
print("Absent Days:", absent)

# 2. Calculate attendance percentage
total_days = len(attendance)
percentage = (present / total_days) * 100
print("Attendance Percentage:", round(percentage, 2), "%")

# 3. Longest consecutive streak of Presence
max_present_streak = 0
current_streak = 0
for ch in attendance:
    if ch == 'P':
        current_streak += 1
        if current_streak > max_present_streak:
            max_present_streak = current_streak
    else:
        current_streak = 0
print("Longest Present Streak:", max_present_streak)

# 4. Longest consecutive streak of Absence
max_absent_streak = 0
current_streak = 0
for ch in attendance:
    if ch == 'A':
        current_streak += 1
        if current_streak > max_absent_streak:
            max_absent_streak = current_streak
    else:
        current_streak = 0
print("Longest Absent Streak:", max_absent_streak)

# 5. Attendance status
if percentage < 75:
    print("Attendance Status: Below 75%")
else:
    print("Attendance Status: Satisfactory")
