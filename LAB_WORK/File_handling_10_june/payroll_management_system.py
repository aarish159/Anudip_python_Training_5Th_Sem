# ---------------- Employee Payroll Management System ----------------
# Problem: Manage employee records stored in employees.txt with operations like
# display, search, average salary, highest/lowest salary, add employee, and categorize salaries.

# Function to load employee data from file
def load_data():
    # Open file in read mode (absolute path used here)
    with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\LAB_WORK\File_handling_10_june\employees.txt", "r") as f:
        data = []
        for line in f:
            # Each line format: EmployeeID,Name,Salary
            emp_id, name, salary = line.strip().split(",")
            data.append((emp_id, name, int(salary)))  # store as tuple
        return data

# 1. Display all employee records
def display_all(data):
    print("\nAll Employee Records:")
    for emp in data:
        print(emp)

# 2. Search employee by Employee ID
def search_employee(data, emp_id):
    for emp in data:
        if emp[0] == emp_id:
            print("\nEmployee Found:", emp)
            return
    print("\nEmployee ID not found!")

# 3. Calculate average salary of all employees
def average_salary(data):
    total = sum(emp[2] for emp in data)  # sum of salaries
    print("\nAverage Salary:", total / len(data))

# 4. Find highest-paid and lowest-paid employee
def highest_lowest(data):
    highest = max(data, key=lambda x: x[2])  # employee with max salary
    lowest = min(data, key=lambda x: x[2])   # employee with min salary
    print("\nHighest Paid:", highest)
    print("Lowest Paid:", lowest)

# 5. Display employees earning above ₹50,000
def above_50k(data):
    print("\nEmployees earning above ₹50,000:")
    for emp in data:
        if emp[2] > 50000:
            print(emp)

# 6. Add a new employee record to the file
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")
    # Open file in append mode to add new record
    with open("employees.txt", "a") as f:
        f.write(f"\n{emp_id},{name},{salary}")
    print("\nEmployee added successfully!")

# 7. Generate salary categories
def salary_categories(data):
    print("\nSalary Categories:")
    for emp in data:
        if emp[2] >= 60000:
            category = "High"
        elif emp[2] >= 40000:
            category = "Medium"
        else:
            category = "Low"
        print(emp, "→", category)

# ------------------- MENU -------------------
while True:
    data = load_data()  # load fresh data each time
    print("\n--- Employee Payroll Management System ---")
    print("1. Display All Records")
    print("2. Search Employee by ID")
    print("3. Calculate Average Salary")
    print("4. Find Highest & Lowest Paid Employee")
    print("5. Display Employees earning above ₹50,000")
    print("6. Add New Employee Record")
    print("7. Generate Salary Categories")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_all(data)
    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        search_employee(data, emp_id)
    elif choice == "3":
        average_salary(data)
    elif choice == "4":
        highest_lowest(data)
    elif choice == "5":
        above_50k(data)
    elif choice == "6":
        add_employee()
    elif choice == "7":
        salary_categories(data)
    elif choice == "8":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
