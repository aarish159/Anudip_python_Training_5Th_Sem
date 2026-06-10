# Student Performance Analytics System

students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 95},
    "S104": {"name": "Neha", "marks": 48},
    "S105": {"name": "Amit", "marks": 67},
    "S106": {"name": "Karan", "marks": 90},
    "S107": {"name": "Meena", "marks": 55},
    "S108": {"name": "Ravi", "marks": 40},
    "S109": {"name": "Simran", "marks": 78},
    "S110": {"name": "Arjun", "marks": 82},
    "S111": {"name": "Sonia", "marks": 33},
    "S112": {"name": "Vikas", "marks": 88},
    "S113": {"name": "Pooja", "marks": 92},
    "S114": {"name": "Deepak", "marks": 60},
    "S115": {"name": "Nisha", "marks": 74},
    "S116": {"name": "Rohan", "marks": 81},
    "S117": {"name": "Alok", "marks": 49},
    "S118": {"name": "Geeta", "marks": 96},
    "S119": {"name": "Manish", "marks": 53},
    "S120": {"name": "Sneha", "marks": 77},
    "S121": {"name": "Kabir", "marks": 84},
    "S122": {"name": "Tina", "marks": 91},
    "S123": {"name": "Varun", "marks": 65},
    "S124": {"name": "Shreya", "marks": 87},
    "S125": {"name": "Ajay", "marks": 46},
    "S126": {"name": "Komal", "marks": 59},
    "S127": {"name": "Nitin", "marks": 71},
    "S128": {"name": "Bhavna", "marks": 93},
    "S129": {"name": "Raj", "marks": 38},
    "S130": {"name": "Pankaj", "marks": 80}
}

# 1. Display all student records
def display_all(students):
    for sid, info in students.items():
        print(sid, "->", info)

# 2. Search student by ID
def search_student(students, sid):
    return students.get(sid, "Not Found")

# 3. Add new student
def add_student(students, sid, name, marks):
    students[sid] = {"name": name, "marks": marks}

# 4. Update marks
def update_marks(students, sid, marks):
    if sid in students:
        students[sid]["marks"] = marks

# 5. Delete student
def delete_student(students, sid):
    if sid in students:
        del students[sid]

# 6. Topper and lowest scorer
def topper_lowest(students):
    topper = max(students.items(), key=lambda x: x[1]["marks"])
    lowest = min(students.items(), key=lambda x: x[1]["marks"])
    return topper, lowest

# 7. Class average
def class_average(students):
    total = sum(info["marks"] for info in students.values())
    return total / len(students)

# 8. Pass/Fail count
def pass_fail(students):
    passed = sum(1 for info in students.values() if info["marks"] >= 50)
    failed = len(students) - passed
    return passed, failed

# 9. Grades
def generate_grades(students):
    grades = {}
    for sid, info in students.items():
        m = info["marks"]
        if m >= 90:
            grade = "A"
        elif m >= 75:
            grade = "B"
        elif m >= 50:
            grade = "C"
        else:
            grade = "F"
        grades[sid] = grade
    return grades

# 10. Students above average
def above_average(students):
    avg = class_average(students)
    return [info["name"] for info in students.values() if info["marks"] > avg]

# 11. Top 5 performers
def top_5(students):
    sorted_students = sorted(students.items(), key=lambda x: x[1]["marks"], reverse=True)
    return sorted_students[:5]

# 12. Scholarship students (marks > 85)
def scholarship_students(students):
    return {sid: info for sid, info in students.items() if info["marks"] > 85}


# ---- Main Execution ----
display_all(students)
print("Search S110:", search_student(students, "S110"))
add_student(students, "S131", "NewStudent", 70)
update_marks(students, "S105", 75)
delete_student(students, "S111")

topper, lowest = topper_lowest(students)
print("Topper:", topper)
print("Lowest:", lowest)

print("Class Average:", round(class_average(students), 2))
passed, failed = pass_fail(students)
print("Passed:", passed, "Failed:", failed)

print("Grades:", generate_grades(students))
print("Above Average Students:", above_average(students))
print("Top 5 Performers:", top_5(students))
print("Scholarship Students:", scholarship_students(students))