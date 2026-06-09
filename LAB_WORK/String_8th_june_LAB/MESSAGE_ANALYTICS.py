# Message stored in chat application
message = "Python is awesome and Python is easy to learn"
print("Message:", message)

# Split into words
words = message.split()

# 1. Count total characters
char_count = 0
for ch in message:
    char_count += 1
print("Total Characters:", char_count)

# 2. Count total words
word_count = 0
for w in words:
    word_count += 1
print("Total Words:", word_count)

# 3. Find longest word
longest_word = ""
for w in words:
    if len(w) > len(longest_word):
        longest_word = w
print("Longest Word:", longest_word)

# 4. Find shortest word
shortest_word = words[0]
for w in words:
    if len(w) < len(shortest_word):
        shortest_word = w
print("Shortest Word:", shortest_word)

# 5. Count occurrences of "Python"
python_count = 0
for w in words:
    if w == "Python":
        python_count += 1
print("Occurrences of Python:", python_count)

# 6. Words having more than 4 characters
long_words = []
for w in words:
    if len(w) > 4:
        long_words.append(w)
print("Words Longer Than 4 Characters:", long_words)

# 7. Words starting with a vowel
vowel_words = []
for w in words:
    if w[0].lower() in ['a','e','i','o','u']:
        vowel_words.append(w)
print("Words Starting With Vowel:", vowel_words)

# 8. Count vowels and consonants
vowels = ['a','e','i','o','u','A','E','I','O','U']
vowel_count = 0
consonant_count = 0
for ch in message:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
