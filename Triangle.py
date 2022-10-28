def is_rightangled(side1, side2, side3):
    if (side1 ** 2 + side2 ** 2 == side3 ** 2) or \
            (side1 ** 2 + side3 ** 2 == side2 ** 2) or \
            (side2 ** 2 + side3 ** 2 == side1 ** 2):
        return True
    else:
        return False


side1 = int(input('Enter Side 1:'))
side2 = int(input('Enter Side 2:'))
side3 = int(input('Enter Side 3:'))

print(is_rightangled(side1, side2, side3))
