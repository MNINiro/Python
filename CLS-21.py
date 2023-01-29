import random

Number = random.randint(1, 100)
TotalTry = 0

Guess = int(input('Enter your guess:'))

while Guess != Number:
    if Guess > Number:
        print("Too large try again")
    else:
        print("Too small try again")

    TotalTry += 1
    Guess = int(input('Enter your guess:'))

# TotalTry -= 1
print("Number of guesses", TotalTry)
