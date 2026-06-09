# Customer review
review = "This product is excellent excellent excellent and very useful"
words = review.split()

# 1. Count total words
word_count = 0
for w in words:
    word_count += 1
print("Total Words:", word_count)

# 2. Word frequencies dictionary
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print("Word Frequencies:")
for word in freq:
    print(word, "->", freq[word])

# 3. Most frequent word
most_word = ""
most_count = 0
for word in freq:
    if freq[word] > most_count:
        most_count = freq[word]
        most_word = word
print("Most Frequent Word:", most_word)

# 4. Words appearing only once
once_words = []
for word in freq:
    if freq[word] == 1:
        once_words.append(word)
print("Words Appearing Once:", once_words)

# 5. Count words > 5 characters
long_count = 0
for w in words:
    if len(w) > 5:
        long_count += 1
print("Words Longer Than 5 Characters:", long_count)

# 6. Words in reverse order
reverse_words = []
for i in range(len(words)-1, -1, -1):
    reverse_words.append(words[i])
print("Words in Reverse Order:", reverse_words)

# 7. Unique words list
unique_words = []
for w in words:
    if w not in unique_words:
        unique_words.append(w)
print("Unique Words:", unique_words)
