# Number Guessing Game without module and function

secret_number = 37   # manually fixed secret number (between 1 and 50)
attempts = 0

print("Guess the secret number between 1 and 50!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct Guess!")
        print("Total attempts:", attempts)
        break
