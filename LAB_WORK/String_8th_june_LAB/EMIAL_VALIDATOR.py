# Email entered
email = "rahul.sharma2026@gmail.com"
print("Email:", email)

# 1. Username (before @)
username = ""
for ch in email:
    if ch == "@":
        break
    username += ch
print("Username:", username)

# 2. Domain and Extension (after @)
after_at = ""
found_at = False
for ch in email:
    if found_at:
        after_at += ch
    if ch == "@":
        found_at = True

domain = ""
extension = ""
dot_found = False
for ch in after_at:
    if ch == "." and not dot_found:
        dot_found = True
        continue
    if not dot_found:
        domain += ch
    else:
        extension += ch

print("Domain:", domain)
print("Extension:", extension)

# 3. Count digits in username
digit_count = 0
for ch in username:
    if ch >= '0' and ch <= '9':
        digit_count += 1
print("Digits Found:", digit_count)

# 4. Count special characters in username
special_count = 0
for ch in username:
    if not (ch.isalpha() or (ch >= '0' and ch <= '9')):
        special_count += 1
print("Special Characters Found:", special_count)

# 5. Check rules
valid = True
if email.count("@") != 1:
    valid = False
if "." not in after_at:
    valid = False

# 6. Status
if valid:
    print("Email Status: Valid")
else:
    print("Email Status: Invalid")