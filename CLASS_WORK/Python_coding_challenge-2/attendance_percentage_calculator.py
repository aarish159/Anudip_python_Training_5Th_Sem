# Problem 18: Student Attendance Percentage Calculator

attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P')

def count_present(attendance):
    present = 0
    for day in attendance:
        if day == 'P':
            present += 1
    return present

def count_absent(attendance):
    absent = 0
    for day in attendance:
        if day == 'A':
            absent += 1
    return absent

def calculate_percentage(present, total):
    return (present / total) * 100

def check_status(percentage):
    if percentage < 75:
        return "Below 75%"
    else:
        return "Eligible"

# ---- Driver Code ----
try:
    total_days = len(attendance)
    present_days = count_present(attendance)
    absent_days = count_absent(attendance)
    percentage = calculate_percentage(present_days, total_days)
    status = check_status(percentage)

    print("Present Days:", present_days)
    print("Absent Days:", absent_days)
    print(f"Attendance Percentage: {percentage:.2f}%")
    print("Attendance Status:", status)

except Exception as e:
    print("Error occurred:", e)
