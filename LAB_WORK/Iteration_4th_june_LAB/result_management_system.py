# Accept marks of 5 subjects
marks = []
failed_subjects = 0

for i in range(1, 6):
    m = int(input(f"Enter marks of subject {i}: "))
    marks.append(m)
    if m < 40:   # fail condition per subject             
        failed_subjects += 1

# Total & Percentage
total = sum(marks)
percentage = total / 5

# Grade Criteria
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Display Results
print("\n--- Result ---")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Subjects Failed:", failed_subjects)