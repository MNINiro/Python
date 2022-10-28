question = "What's the capital of Germany? "
attempts = 0

while True:
    attempts = attempts + 1
    response = input("Attempt #" + str(attempts) + " | " + question)

    if response.lower() == "berlin":
        print("Correct! Thanks for playing")
        break
    else:
        print("Incorrect.")
        if attempts == 1:
            print("Hint: An American president once said:",
                  "Ich bin ein ........")
        if attempts == 2:
            print("Hint: In the Cold War, a wall split this city.")
        if attempts == 3:
            print("Hint: the city name starts with a 'B'.")