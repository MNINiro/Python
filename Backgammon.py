import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
sum = 0

print('Dice1:', dice1)
print('Dice2:', dice2)
print()

if dice1 == dice2:
    sum = 2 * (dice1 + dice2)
    print(sum)
else:
    sum = dice1 + dice2
    print(sum)
