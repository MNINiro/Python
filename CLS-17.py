# you have maximum 3 chances to guess
# if guess matches then you are the winner and code will stop
# otherwise, code will run for 3 times then show sorry message

import random

data = random.randint(0, 9)
counter = 0

while counter <= 2:
    guess = int(input('Enter your guess:'))
    if data == guess:
        print("Winner")
        break
    elif counter != 2:
        print("Try again")
    else:
        print('Sorry, you are the loser')
    counter += 1




