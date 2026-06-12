# Library Book Issues Analysis System

book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

# 1. Find maximum number of issues
max_issues = book_issues[0]
for issue in book_issues:
    if issue > max_issues:
        max_issues = issue
print("Maximum Issues:", max_issues)

# 2. Find minimum number of issues
min_issues = book_issues[0]
for issue in book_issues:
    if issue < min_issues:
        min_issues = issue
print("Minimum Issues:", min_issues)

# 3. Calculate average number of issues
total = 0
for issue in book_issues:
    total += issue
average = total / len(book_issues)
print("Average Issues:", round(average, 1))

# 4. Count books issued more than 15 times
count_more = 0
for issue in book_issues:
    if issue > 15:
        count_more += 1
print("Books Issued More Than 15 Times:", count_more)

# 5. Create a list of books issued fewer than 10 times
fewer_list = []
for issue in book_issues:
    if issue < 10:
        fewer_list.append(issue)
print("Books Issued Fewer Than 10 Times:", fewer_list)
