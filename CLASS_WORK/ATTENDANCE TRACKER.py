# Attendance Tracker Program

# Total students in class
total_students = 30

# Counters
present_count = 0
absent_count = 0

# Loop through each student
for i in range(1, total_students + 1):
    status = input(f"Student {i} Attendance (Present/Absent): ").strip().lower()
    
    if status == "present":
        present_count += 1
        print(f"Student {i} Attendance : Present")
    elif status == "absent":
        absent_count += 1
        print(f"Student {i} Attendance : Absent")
    else:
        print("Invalid input! Marking Absent by default.")
        absent_count += 1

# Final summary
print("\nAttendance Summary:")
print(f"No. of Students Present : {present_count}")
print(f"No. of Students Absent  : {absent_count}")
