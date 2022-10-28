pi = 3.14  # Global variable


def add(x, y):  # local variable
    z = x + y
    print('Addition:', z)
    return z


def sub(x, y):  # local variable
    z = x - y
    print('Subtraction:', z)
    temp = add(10, 10)
    print('Calculated result:', z + temp)
    return z


# =========Main Body==========
d1 = int(input('Enter 1st data:'))
d2 = int(input('Enter 2nd data:'))
# print('Outside function:', add(d1, d2))  # parameter passing
# print('Result of sub', sub(d1, d2))

print('Multiplication:', add(d1, d2) * sub(d1, d2) + pi)
