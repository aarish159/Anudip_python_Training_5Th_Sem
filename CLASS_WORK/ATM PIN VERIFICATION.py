# ATM PIN Verification Program

# Valid PIN
valid_pin = "1234"

# Loop until correct PIN is entered
while True:
    pin = input("Enter PIN: ").strip()
    
    if pin == valid_pin:
        print("Access Granted.")
        break
    else:
        print("Incorrect PIN. Try Again.")
