# Reviews list
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# 1. Count sentiments
def count_sentiments(reviews):
    excellent = good = average = poor = 0
    for r in reviews:
        if "excellent" in r:
            excellent += 1
        elif "good" in r:
            good += 1
        elif "average" in r:
            average += 1
        elif "poor" in r:
            poor += 1
    return excellent, good, average, poor

# 2. Most common word
def most_common_word(reviews):
    words = []
    for r in reviews:
        words.extend(r.split())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return max(freq, key=freq.get)

# 3. Longest review
def longest_review(reviews):
    longest = reviews[0]
    for r in reviews:
        if len(r) > len(longest):
            longest = r
    return longest

# 4. Reviews with keyword
def reviews_with_keyword(reviews, keyword):
    result = []
    for r in reviews:
        if keyword in r:
            result.append(r)
    return result


# ---- Main Execution ----
excellent, good, average, poor = count_sentiments(reviews)
print("Excellent Reviews:", excellent)
print("Good Reviews:", good)
print("Average Reviews:", average)
print("Poor Reviews:", poor)

print("Most Common Word:", most_common_word(reviews))
print("Longest Review:", longest_review(reviews))

keyword = "excellent"
print(f"Reviews containing '{keyword}':")
for r in reviews_with_keyword(reviews, keyword):
    print(r)
