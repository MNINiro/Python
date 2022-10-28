def PirateShip(gold, pirate):
    success = False
    total = gold + pirate

    if total > 100:
        print('Ship sunk')
        return success
    else:
        if gold < pirate:
            print('0-Bad')
        elif gold == pirate:
            print('1-Good')
        elif gold % pirate == 0:
            print('2-Great')

        success = True
        return success


g = int(input('Enter gold:'))
p = int(input('Enter pirates:'))
x = PirateShip(g, p)
print(x)

