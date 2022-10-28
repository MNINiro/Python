# There are few integer elements in an array.
# Select a pair of integers from the array that will make
# the asked value as an output
# Use function with parameters

import random

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
val = []


def matchingPair(op):
    for counter in range(len(lst)):
        x = random.choice(lst)  # selecting random value from the lst list
        if x not in val:  # checking if the value of x not in the val list
            y = op - x  # generating remaining value to form the pair
            if y in lst:  # it will select the remaining value if it is only available in the lst list
                print(x, '+', y, '=', op)
        val.append(x)  # to make unique pair
        # print(val)


def matchingPairAlt(op):
    for counter in range(len(lst)):
        x = random.choice(lst)  # selecting random value from the lst list
        y = random.randrange(len(lst))  # selecting random value from the lst list
        print(x, ' ', y)
        if x + y == op:
            print(x, '+', y, '=', op)

        # if x not in val:  # checking if the value of x not in the val list
        #     if x + y == op:
        #         print(x, '+', y, '=', op)
        # val.append(x)  # to make unique pair


# ============ Main Body ============

target = int(input('Enter target value:'))
matchingPair(target)
print()
print("=========================")
matchingPairAlt(target)
