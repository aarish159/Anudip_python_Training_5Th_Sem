# Employee Salary Report Generator

# Read employee data from file
with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_coding_challenge-2\employees.txt", "r") as f:
    lines = f.readlines()

# Convert data into dictionary {Name: Salary}
employees = {}
for line in lines:
    parts = line.strip().split(",")
    emp_id = parts[0]
    name = parts[1]
    salary = int(parts[2])
    employees[name] = salary

# 1. Display employees earning more than ₹50,000
print("Employees Earning Above ₹50,000:", end=" ")
for name in employees:
    if employees[name] > 50000:
        print(name, end=" ")
print()

# 2. Find highest-paid employee
highest_name = None
highest_salary = -1
for name in employees:
    if employees[name] > highest_salary:
        highest_salary = employees[name]
        highest_name = name
print("Highest Paid Employee:", highest_name, "(₹", highest_salary, ")")

# 3. Find lowest-paid employee
lowest_name = None
lowest_salary = 999999
for name in employees:
    if employees[name] < lowest_salary:
        lowest_salary = employees[name]
        lowest_name = name
print("Lowest Paid Employee:", lowest_name, "(₹", lowest_salary, ")")

# 4. Calculate average salary
total_salary = 0
for name in employees:
    total_salary += employees[name]
average_salary = total_salary / len(employees)
print("Average Salary: ₹", round(average_salary))

# 5. Generate salary categories
high = []
medium = []
low = []
for name in employees:
    if employees[name] >= 60000:
        high.append(name)
    elif 40000 <= employees[name] < 60000:
        medium.append(name)
    else:
        low.append(name)

print("High Salary:", high)
print("Medium Salary:", medium)
print("Low Salary:", low)