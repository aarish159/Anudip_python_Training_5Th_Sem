# Problem: Plagiarism Review Analyzer

abstract1 = "Artificial intelligence is transforming education and healthcare."
abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence."

def convert_to_set(text):
    words = text.lower().replace(".", "").split()
    return set(words)

def common_words(set1, set2):
    return set1.intersection(set2)

def unique_words(set1, set2):
    return set1.difference(set2), set2.difference(set1)

def similarity_percentage(set1, set2):
    common = len(set1.intersection(set2))
    total_unique = len(set1.union(set2))
    return (common / total_unique) * 100

def plagiarism_review(similarity):
    if similarity > 50:
        return "Yes"
    else:
        return "No"

# ---- Driver Code ----
set1 = convert_to_set(abstract1)
set2 = convert_to_set(abstract2)

common = common_words(set1, set2)
unique1, unique2 = unique_words(set1, set2)
similarity = similarity_percentage(set1, set2)
review = plagiarism_review(similarity)

print("Common Words:", common)
print("Unique Words in Abstract 1:", unique1)
print("Unique Words in Abstract 2:", unique2)
print(f"Similarity Percentage: {similarity:.1f}%")
print("Plagiarism Review Required:", "Yes" if review == "Yes" else "No")
