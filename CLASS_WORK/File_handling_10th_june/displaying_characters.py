# ---------------- File Handling Program ----------------
# Problem: Read data from a file and display
# 1. Number of vowels
# 2. Number of characters
# 3. Number of lines

# Define vowels (both uppercase and lowercase)
vowels = "aeiouAEIOU"

# Initialize counters
vowel_count = 0
char_count = 0
line_count = 0

# Open the file in read mode
# Use absolute path to ensure Python finds the file correctly
with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\File_handling_10th_june\sample.txt", "r") as f:
    # Read file line by line
    for line in f:
        line_count += 1  # Count each line
        for ch in line:  # Loop through each character in the line
            char_count += 1  # Count characters
            if ch in vowels:  # Check if character is a vowel
                vowel_count += 1  # Count vowels

# Display results
print("Number of Vowels:", vowel_count)
print("Number of Characters:", char_count)
print("Number of Lines:", line_count)
