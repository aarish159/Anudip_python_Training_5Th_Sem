# Prime number check

num = int(input("Enter a number: "))

if num > 1:   # prime numbers are greater than 1
    for i in range(2, int(num**0.5) + 1):  # check till sqrt(num)
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
else:
    print(num, "is NOT a prime number")
