# Attendance Counter Program in Python

# List of students
students = ["Aarish", "Rahul", "Priya", "Neha", "Amit"]

# Dictionary to store attendance
attendance = {}

print("Mark attendance: (P for Present / A for Absent)\n")

# Taking attendance input
for student in students:
    status = input(f"{student}: ").strip().upper()
    if status == "P":
        attendance[student] = "Present"
    elif status == "A":
        attendance[student] = "Absent"
    else:
        print("Invalid input! Marking Absent by default.")
        attendance[student] = "Absent"

# Counting attendance
present_count = sum(1 for s in attendance.values() if s == "Present")
absent_count = sum(1 for s in attendance.values() if s == "Absent")

# Display result
print("\nAttendance Summary:")
print(f"Total Students: {len(students)}")
print(f"Present: {present_count}")
print(f"Absent: {absent_count}")

print("\nDetailed Report:")
for student, status in attendance.items():
    print(f"{student}: {status}")
