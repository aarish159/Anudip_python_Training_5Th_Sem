# License key entered
license_key = "ABCD-EFGH-IJKL-MNOP"
print("License Key:", license_key)

# 1. Split into groups
groups = license_key.split("-")
print("Groups:", groups)

# 2. Verify number of groups
num_groups = 0
for g in groups:
    num_groups += 1
print("Number of Groups:", num_groups)

# 3. Verify each group has 4 characters
valid = True
for g in groups:
    if len(g) != 4:
        valid = False

# 4. Count total letters
letter_count = 0
for ch in license_key:
    if ch >= 'A' and ch <= 'Z':
        letter_count += 1
print("Total Letters:", letter_count)

# 5. Count vowels
vowels = ['A','E','I','O','U']
vowel_count = 0
for ch in license_key:
    if ch in vowels:
        vowel_count += 1
print("Total Vowels:", vowel_count)

# 6. Remove hyphens and display merged key
merged_key = ""
for ch in license_key:
    if ch != "-":
        merged_key += ch
print("Merged Key:", merged_key)

# 7. Display status
if num_groups == 4 and valid == True:
    print("License Key Status: Valid")
else:
    print("License Key Status: Invalid")
