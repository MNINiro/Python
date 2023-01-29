# Ludo game
import random

p1_start = False
p2_start = False

green = 0
red = 0

while green <= 49 or red <= 49:
    player1 = input("Enter Player 1:").upper()
    if player1 == "A":
        dice = random.randint(1, 6)
        print('Player-1:', dice)
        if green == 0 and dice == 6:
            p1_start = True
            dice = random.randint(1, 6)            print('Player-1 next move:', dice)
            green += dice
            print(green)
        elif green != 0:
            dice = random.randint(1, 6)
            print('Player-1:', dice)
            green += dice
            print("Green:", green)
            if green >= 49:
                print(player1, " is the winner")
                break

    player2 = input("Enter Player 2:").upper()
    if player2 == "B":
        dice = random.randint(1, 6)
        print('Player-2:', dice)
        if dice == 6:
            p2_start = True
            dice = random.randint(1, 6)
            print('Player-2 next move:', dice)
            red += dice
            print(red)
        elif red != 0:
            dice = random.randint(1, 6)
            print('Player-2:', dice)
            red += dice
            print("Red:", red)
            if red >= 49:
                print(player2, "is the winner")
                break
