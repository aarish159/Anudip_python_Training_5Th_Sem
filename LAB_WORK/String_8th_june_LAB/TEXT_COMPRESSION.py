# Compressed message
text = "AAABBBCCCDDDAAA"
print("Original Text:", text)

# 1. Count occurrences of each character
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequencies:")
for ch in freq:
    print(ch, "->", freq[ch])

# 2. Dictionary already created above (freq)

# 3. Display unique characters
unique_chars = []
for ch in freq:
    unique_chars.append(ch)
print("Unique Characters:", unique_chars)

# 4. Find most frequent character
most_char = ""
most_count = 0
for ch in freq:
    if freq[ch] > most_count:
        most_count = freq[ch]
        most_char = ch
print("Most Frequent Character:", most_char)

# 5. Create compressed output (run-length encoding)
compressed = ""
count = 1
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        count += 1
    else:
        compressed += text[i-1] + str(count)
        count = 1
compressed += text[-1] + str(count)  # last group
print("Compressed Output:", compressed)

# 6. Calculate compression ratio
original_len = len(text)
compressed_len = len(compressed)
ratio = (compressed_len / original_len) * 100

print("Original Length:", original_len)
print("Compressed Length:", compressed_len)
print("Compression Ratio:", round(ratio, 2), "%")
