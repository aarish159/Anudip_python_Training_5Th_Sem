employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# 1. Display employees earning above ₹50,000
print("Employees earning above ₹50,000:")
for emp in employees:
    if emp[1] > 50000:
        print(emp[0], emp[1])

# 2. Find the highest-paid employee
highest = employees[0]   # assume first employee
for emp in employees:
    if emp[1] > highest[1]:
        highest = emp
print("\nHighest Paid Employee:", highest[0], highest[1])

# 3. Calculate total salary expenditure
total_salary = 0
for emp in employees:
    total_salary += emp[1]
print("\nTotal Salary Expenditure: ₹", total_salary)

# 4. Count employees earning below ₹40,000
below_40k = 0
for emp in employees:
    if emp[1] < 40000:
        below_40k += 1
print("\nEmployees earning below ₹40,000:", below_40k)
