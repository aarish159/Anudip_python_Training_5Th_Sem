# Student Scholarship Evaluation System

#guven data
marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}

# Students scoring above 85
def above_85(marks):
    result = []
    for name in marks:
        if marks[name] > 85:
            result.append(name)
    return result

#  Topper
def topper(marks):
    top = list(marks.keys())[0]
    for name in marks:
        if marks[name] > marks[top]:
            top = name
    return top, marks[top]

# Lowest scorer
def lowest(marks):
    low = list(marks.keys())[0]
    for name in marks:
        if marks[name] < marks[low]:
            low = name
    return low, marks[low]

# Class average
def average(marks):
    total = 0
    count = 0
    for name in marks:
        total += marks[name]
        count += 1
    return total / count

# Generate grades
def generate_grades(marks):
    grades = {}
    for name in marks:
        m = marks[name]
        if m >= 90:
            grades[name] = "A"
        elif m >= 75:
            grades[name] = "B"
        elif m >= 50:
            grades[name] = "C"
        else:
            grades[name] = "F"
    return grades

# Scholarship students (marks ≥ 90)
def scholarship(marks):
    result = []
    for name in marks:
        if marks[name] >= 90:
            result.append(name)
    return result

# output
print("Students Scoring Above 85:", above_85(marks))

top = topper(marks)
print("Topper:", top[0], "(", top[1], "marks)")

low = lowest(marks)
print("Lowest Scorer:", low[0], "(", low[1], "marks)")

print("Average Marks:", round(average(marks), 1))

print("Grades:", generate_grades(marks))

print("Scholarship Students:", scholarship(marks))
