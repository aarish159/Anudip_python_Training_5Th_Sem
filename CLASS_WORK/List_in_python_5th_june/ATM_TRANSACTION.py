# Transactions list
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# 1. Calculate current balance
balance = 0
for t in transactions:
    balance += t

# 2. Separate deposits and withdrawals
deposits = []
withdrawals = []
for t in transactions:
    if t > 0:
        deposits.append(t)
    else:
        withdrawals.append(t)

# 3. Count total deposits and withdrawals
deposit_count = len(deposits)
withdrawal_count = len(withdrawals)

# 4. Find largest deposit and largest withdrawal (without max/min)
largest_deposit = deposits[0]
for d in deposits:
    if d > largest_deposit:
        largest_deposit = d

largest_withdrawal = withdrawals[0]
for w in withdrawals:
    if w < largest_withdrawal:   # more negative = larger withdrawal
        largest_withdrawal = w

# Output
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
