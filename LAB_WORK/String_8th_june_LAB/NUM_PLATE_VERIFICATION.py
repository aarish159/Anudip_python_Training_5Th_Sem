# Vehicle number plate entered
plate = "MH12AB4589"
print("Vehicle Number:", plate)

# 1. Extract state code
state_code = plate[0:2]
print("State Code:", state_code)

# 2. Extract district code
district_code = plate[2:4]
print("District Code:", district_code)

# 3. Extract vehicle series
series = plate[4:6]
print("Series:", series)

# 4. Extract vehicle number
vehicle_number = plate[6:]
print("Vehicle Number:", vehicle_number)

# 5. Count letters and digits separately
letter_count = 0
digit_count = 0
for ch in plate:
    if ch >= 'A' and ch <= 'Z':   # simple check for letters
        letter_count += 1
    elif ch >= '0' and ch <= '9': # simple check for digits
        digit_count += 1
print("Total Letters:", letter_count)
print("Total Digits:", digit_count)

# 6. Verify rules step by step
valid = True
if not (plate[0:2].isalpha()):
    valid = False
if not (plate[2:4].isdigit()):
    valid = False
if not (plate[4:6].isalpha()):
    valid = False
if not (plate[6:].isdigit()):
    valid = False

# 7. Display status
if valid == True:
    print("Vehicle Number Status: Valid")
else:
    print("Vehicle Number Status: Invalid")
