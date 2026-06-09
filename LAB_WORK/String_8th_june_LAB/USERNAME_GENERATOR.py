# Original name entered
name = "Rahul Sharma"
print("Original Name:", name)

# 1. Remove spaces
username = ""
for ch in name:
    if ch != " ":
        username += ch

# 2. Convert to lowercase
username = username.lower()

# 3. Append current year (2026)
username = username + "2026"

# 4. If length > 12, keep only first 12 characters
if len(username) > 12:
    username = username[:12]

print("Generated Username:", username)

# 5. Count vowels
vowels = ['a','e','i','o','u']
vowel_count = 0
for ch in username:
    if ch in vowels:
        vowel_count += 1

# 6. Count consonants
consonant_count = 0
for ch in username:
    if ch.isalpha() and ch not in vowels:
        consonant_count += 1

# 7. Display statistics
print("Username Length:", len(username))
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Status: Username Generated Successfully")
