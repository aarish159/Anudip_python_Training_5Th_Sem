emp_id = "EMP2026ANUJ458"
print("Employee ID:", emp_id)

# 1. Count uppercase letters
upper_count = 0
for ch in emp_id:
    if ch >= 'A' and ch <= 'Z':   # simple check
        upper_count += 1
print("Uppercase Letters:", upper_count)

# 2. Count digits
digit_count = 0
for ch in emp_id:
    if ch >= '0' and ch <= '9':   # simple check
        digit_count += 1
print("Digits:", digit_count)

# 3. Extract joining year
joining_year = emp_id[3:7]
print("Joining Year:", joining_year)

# 4. Extract employee name
employee_name = emp_id[7:-3]
print("Employee Name:", employee_name)

# 5. Check rules (step by step)
valid = True
if emp_id[0:3] != "EMP":
    valid = False
if emp_id[3:7].isdigit() == False:
    valid = False
if emp_id[-3:].isdigit() == False:
    valid = False

# 6. Create list of digits
digit_list = []
for ch in emp_id:
    if ch >= '0' and ch <= '9':
        digit_list.append(int(ch))
print("Digit List:", digit_list)

# 7. Sum of digits
digit_sum = 0
for d in digit_list:
    digit_sum += d
print("Sum of Digits:", digit_sum)

# 8. Display status
if valid == True:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")
