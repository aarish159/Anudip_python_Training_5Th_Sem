# Employee Payroll Management System

def load_data():
    with open("employees.txt", "r") as f:
        data = []
        for line in f:
            emp_id, name, salary = line.strip().split(",")
            data.append((emp_id, name, int(salary)))
        return data

def display_all(data):
    print("\nAll Employee Records:")
    for emp in data:
        print(emp)

def search_employee(data, emp_id):
    for emp in data:
        if emp[0] == emp_id:
            print("\nEmployee Found:", emp)
            return
    print("\nEmployee ID not found!")

def average_salary(data):
    total = sum(emp[2] for emp in data)
    print("\nAverage Salary:", total / len(data))

def highest_lowest(data):
    highest = max(data, key=lambda x: x[2])
    lowest = min(data, key=lambda x: x[2])
    print("\nHighest Paid:", highest)
    print("Lowest Paid:", lowest)

def above_50k(data):
    print("\nEmployees earning above ₹50,000:")
    for emp in data:
        if emp[2] > 50000:
            print(emp)

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")
    with open("employees.txt", "a") as f:
        f.write(f"\n{emp_id},{name},{salary}")
    print("\nEmployee added successfully!")

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
    data = load_data()
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