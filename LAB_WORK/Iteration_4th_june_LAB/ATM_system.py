# Initial Balance
balance = 10000

while True:
    print("\n--- Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("₹", amount, "deposited successfully.")
        print("Updated Balance: ₹", balance)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient Balance! Withdrawal not allowed.")
        else:
            balance -= amount
            print("₹", amount, "withdrawn successfully.")
            print("Updated Balance: ₹", balance)

    elif choice == 4:
        print("Thank you! Exiting program...")
        break

    else:
        print("Invalid choice! Please select 1-4.")
