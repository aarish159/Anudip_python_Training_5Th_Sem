# Numbers list
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# List to store consecutive pairs
consecutive_pairs = []

# Loop through list
for i in range(len(numbers) - 1):
    if numbers[i+1] - numbers[i] == 1:   # check consecutive
        print(numbers[i], "and", numbers[i+1], "are consecutive")
        consecutive_pairs.append((numbers[i], numbers[i+1]))

# Print final list of pairs
print("Consecutive Pairs List:", consecutive_pairs)
