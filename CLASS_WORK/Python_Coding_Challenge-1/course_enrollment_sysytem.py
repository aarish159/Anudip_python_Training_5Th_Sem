# University Course Enrollment Analysis

enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}

# 1. Display courses having more than 40 enrollments
def high_enrollment(data):
    print("Courses with More Than 40 Enrollments:", end=" ")
    for course in data:
        if data[course] > 40:
            print(course, end=" ")
    print()

# 2. Find most and least popular courses
def extremes(data):
    max_course = ""
    min_course = ""
    max_val = -1
    min_val = 999999
    for course in data:
        val = data[course]
        if val > max_val:
            max_val = val
            max_course = course
        if val < min_val:
            min_val = val
            min_course = course
    print(f"Most Popular Course: {max_course} ({max_val} students)")
    print(f"Least Popular Course: {min_course} ({min_val} students)")
    return max_val, min_val

# 3. Calculate total enrollments
def total_enrollments(data):
    total = 0
    for course in data:
        total += data[course]
    print("Total Enrollments:", total)
    return total

# 4. Categorize courses
def categorize(data):
    high = []
    medium = []
    low = []
    for course in data:
        val = data[course]
        if val > 40:
            high.append(course)
        elif val >= 30 and val <= 40:
            medium.append(course)
        else:
            low.append(course)
    print("High Demand:", high)
    print("Medium Demand:", medium)
    print("Low Demand:", low)
    return high, medium, low

# 5. Count courses requiring promotion (<35 enrollments)
def promotion(data):
    count = 0
    for course in data:
        if data[course] < 35:
            count += 1
    print("Courses Requiring Promotion:", count)


# function call
high_enrollment(enrollment)
extremes(enrollment)
total_enrollments(enrollment)
categorize(enrollment)
promotion(enrollment)
