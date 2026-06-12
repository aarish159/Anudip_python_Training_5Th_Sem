# Student Feedback Analysis System

# Open the file in read mode
with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_coding_challenge-2\feedback.txt", "r") as f:
    lines = f.readlines()

# 1. Count total number of lines
total_lines = len(lines)

# 2. Count total number of words
total_words = 0
for line in lines:
    words = line.split()
    total_words += len(words)

# 3. Count total number of characters
total_chars = 0
for line in lines:
    total_chars += len(line)

# 4. Find longest feedback comment
longest = lines[0].strip()
for line in lines:
    if len(line.strip()) > len(longest):
        longest = line.strip()

# 5. Find shortest feedback comment
shortest = lines[0].strip()
for line in lines:
    if len(line.strip()) < len(shortest):
        shortest = line.strip()

# 6. Count total vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for line in lines:
    for ch in line:
        if ch in vowels:
            vowel_count += 1

# --- Output ---
print("Total Lines:", total_lines)
print("Total Words:", total_words)
print("Total Characters:", total_chars)
print("Longest Feedback:", longest)
print("Shortest Feedback:", shortest)
print("Total Vowels:", vowel_count)
