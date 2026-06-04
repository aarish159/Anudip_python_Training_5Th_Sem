# Mini Employee Payroll System

# Input
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# Components
hra = 0.20 * basic_salary   # 20% of basic
da  = 0.10 * basic_salary   # 10% of basic
pf  = 0.12 * basic_salary   # 12% deduction

# Gross & Net Salary
gross_salary = basic_salary + hra + da
net_salary   = gross_salary - pf

# Grade Decision
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# Display
print("\n--- Employee Payroll ---")
print("Employee Name:", name)
print("Basic Salary: ₹", basic_salary)
print("HRA (20%): ₹", hra)
print("DA (10%): ₹", da)
print("PF Deduction (12%): ₹", pf)
print("Gross Salary: ₹", gross_salary)
print("Net Salary: ₹", net_salary)
print("Grade:", grade)
