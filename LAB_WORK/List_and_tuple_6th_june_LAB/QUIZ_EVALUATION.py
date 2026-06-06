correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

# 1. Calculate score
score = 0
for i in range(len(correct)):
    if student[i] == correct[i]:
        score += 1
print("Score:", score, "out of", len(correct))

# 2. Display incorrectly answered question numbers
print("\nIncorrectly Answered Questions:")
for i in range(len(correct)):
    if student[i] != correct[i]:
        print("Question", i + 1)

# 3. Count correct and wrong answers
correct_count = 0
wrong_count = 0
for i in range(len(correct)):
    if student[i] == correct[i]:
        correct_count += 1
    else:
        wrong_count += 1
print("\nCorrect Answers:", correct_count)
print("Wrong Answers:", wrong_count)

# 4. Determine pass/fail (minimum 60%)
percentage = (score / len(correct)) * 100
print("\nPercentage:", percentage, "%")
if percentage >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")
