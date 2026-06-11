# Student Marks Management System

# 1. Calculate grades and generate report card
def generate_report():
    f = open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_Coding_Challenge-1\marks.txt", "r")
    out = open("report_card.txt", "w")

    passed = 0
    failed = 0
    topper_name = ""
    topper_marks = -1
    merit = []

    for line in f:
        data = line.strip().split(",")
        sid = data[0]
        name = data[1]
        marks = int(data[2])

        # Grade calculation
        if marks >= 90:
            grade = "A"
            merit.append(name)
        elif marks >= 75:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "F"

        # Pass/Fail count
        if marks >= 40:
            passed += 1
        else:
            failed += 1

        # Topper check
        if marks > topper_marks:
            topper_marks = marks
            topper_name = name

        # Write to report_card.txt
        out.write(f"{sid},{name},{marks},{grade}\n")

    f.close()
    out.close()

# Display results
    print("Topper:", topper_name, f"({topper_marks})")
    print("Merit Certificate Holders:", *merit)
    print("Passed Students:", passed, "Failed Students:", failed)
    print("Report Cards Generated Successfully.")
    

# function call
generate_report()
