def AddTemp():
    x = 10
    y = 12
    z = x * y
    print('Result is', z)


def add(arg1, arg2):  # Add both the parameters and return them.
    total1 = arg1 + arg2
    print("Inside addition : ", total1)
    return total1


def sub(arg1, arg2):  # Subtract and return them.
    total2 = arg1 - arg2
    print("Inside subtraction : ", total2)

    x1 = add(4, 4)
    x2 = x1 + total2
    print("Temporary:", x2)
    return total2


# ======== Main Body ==================
# AddTemp()

# add(10,15)
# add(20,15)
# add(30,15)

# x = int(input('Enter 1st Data :'))
# y = int(input('Enter 2nd Data :'))
# add(x, y)

# sub(x, y)
# z = x+y
# add(z,x)

print("Outside function, addition :",add(10,20)+50)
# print("Outside function, subtraction :",sub(20,15)+50)
# print("Outside function, addition & subtraction :",add(10,20) + sub(15,5)+50)
