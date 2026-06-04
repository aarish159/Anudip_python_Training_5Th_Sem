print("------------ Simple Interest ------------")

p = float(input("ENTER PRINCIPAL AMOUNT: "))
r = float(input("ENTER RATE OF INTEREST: "))
t = float(input("ENTER TIME: "))

if p > 0 and r > 0 and t > 0:
    si = (p * r * t) / 100
    print("Simple Interest =", si)
else:
    print("Invalid Data! Enter positive values only.")