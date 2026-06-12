# Problem 19: Article Word Analyzer

def read_file():
    try:
        with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_coding_challenge-2\article.txt", "r") as f:   
            data = f.read()
        return data
    except FileNotFoundError:
        print("Error: article.txt not found.")
        return ""

def count_words(text):
    words = text.split()
    return len(words), words

def word_frequency(words):
    freq = {}
    for w in words:
        w = w.strip(".").lower()   # normalize words
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

def most_frequent_word(freq):
    max_word = None
    max_count = 0
    for word, count in freq.items():
        if count > max_count:
            max_word = word
            max_count = count
    return max_word, max_count

def words_once(freq):
    once = []
    for word, count in freq.items():
        if count == 1:
            once.append(word)
    return once

def unique_words(freq):
    return set(freq.keys())

# ---- Driver Code ----
text = read_file()
if text:
    total, words = count_words(text)
    freq = word_frequency(words)
    most_word, most_count = most_frequent_word(freq)
    once_words = words_once(freq)
    unique = unique_words(freq)

    print("Total Words:", total)
    print(f"Most Frequent Word: {most_word.capitalize()} ({most_count} times)")
    print("Words Appearing Once:", " ".join(once_words))
    print("Unique Words Count:", len(unique))
