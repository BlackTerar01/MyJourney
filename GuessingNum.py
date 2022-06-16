import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < randomNumber:
            print("Sorry, guess again. Too low.")
        elif guess > randomNumber:
            print("Sorry, guess again. Too high.")
    print(f"Yay, congrats. You have guessed the number {randomNumber} correctly.")

def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay! The computer guessed your number {guess}, correctly!")

computerGuess(15)
#guess(10)