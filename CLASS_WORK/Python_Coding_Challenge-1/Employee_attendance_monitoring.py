# Employee Attendance Management System

def attendance_system():
    # 1. Count present and absent employees
    f = open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_Coding_Challenge-1\attendance.txt", "r")
    present = 0
    absent = 0
    absent_ids = []

    for line in f:
        data = line.strip().split(",")
        emp_id = data[0]
        status = data[1]

        if status == "P":
            present += 1
        else:
            absent += 1
            absent_ids.append(emp_id)

    f.close()

    print("Present Employees:", present)
    print("Absent Employees:", absent)

    # 2. Display absent employee IDs
    print("Absent Employee IDs:", *absent_ids)

    # 3. Attendance percentage
    total = present + absent
    percent = (present / total) * 100
    print("Attendance Percentage:", str(percent) + "%")

    # 4. Generate absentee report
    out = open("absent_report.txt", "w")
    for emp in absent_ids:
        out.write(emp + "\n")
    out.close()
    print("Absentee Report Generated Successfully.")

    # 5. Attendance award eligibility
    if absent == 0:
        print("Attendance Award Eligibility: Applicable")
    else:
        print("Attendance Award Eligibility: Not Applicable")


# function call
attendance_system()
