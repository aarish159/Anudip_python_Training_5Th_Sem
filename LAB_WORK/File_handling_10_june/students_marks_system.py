# ---------------- Student Marks Management System ----------------
# Problem: Manage student marks stored in results.txt with operations like
# display, search, topper, average, pass/fail count, grade generation,
# and writing grade reports into grades.txt.

# Function to load student data from file
def load_data():
    with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\LAB_WORK\File_handling_10_june\result.txt", "r") as f:
        data = []
        for line in f:
            # Each line format: StudentID,Name,Marks
            sid, name, marks = line.strip().split(",")
            data.append((sid, name, int(marks)))  # store as tuple
        return data

# Function to save grade reports into grades.txt
def save_grades(grades):
    with open("grades.txt", "w") as f:
        for g in grades:
            f.write(f"{g[0]},{g[1]},{g[2]},{g[3]}\n")

# 1. Display all student records
def display_all(data):
    print("\nAll Student Records:")
    for stu in data:
        print(stu)

# 2. Search student by Student ID
def search_student(data, sid):
    for stu in data:
        if stu[0] == sid:
            print("\nStudent Found:", stu)
            return
    print("\nStudent ID not found!")

# 3. Find topper and lowest scorer
def topper_lowest(data):
    topper = max(data, key=lambda x: x[2])   # student with max marks
    lowest = min(data, key=lambda x: x[2])   # student with min marks
    print("\nTopper:", topper)
    print("Lowest Scorer:", lowest)

# 4. Calculate class average
def class_average(data):
    total = sum(stu[2] for stu in data)
    print("\nClass Average:", total / len(data))

# 5. Count pass and fail students (pass = marks >= 40)
def pass_fail_count(data):
    passed = sum(1 for stu in data if stu[2] >= 40)
    failed = len(data) - passed
    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

# 6. Generate grades and write to grades.txt
def generate_grades(data):
    grades = []
    for stu in data:
        marks = stu[2]
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "F"
        grades.append((stu[0], stu[1], marks, grade))
    save_grades(grades)
    print("\nGrades generated and saved to grades.txt")
    for g in grades:
        print(g)

# ------------------- MENU -------------------
while True:
    data = load_data()  # load fresh data each time
    print("\n--- Student Marks Management System ---")
    print("1. Display All Records")
    print("2. Search Student by ID")
    print("3. Find Topper & Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass & Fail Students")
    print("6. Generate Grades and Save to File")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_all(data)
    elif choice == "2":
        sid = input("Enter Student ID: ")
        search_student(data, sid)
    elif choice == "3":
        topper_lowest(data)
    elif choice == "4":
        class_average(data)
    elif choice == "5":
        pass_fail_count(data)
    elif choice == "6":
        generate_grades(data)
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
