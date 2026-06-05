# Login System Program

# Correct password
correct_password = "admin123"

# Keep asking until correct password is entered
while True:
    password = input("Enter Password: ").strip()
    
    if password == correct_password:
        print("Login Successful.")
        break
    else:
        print("Invalid Password.")
