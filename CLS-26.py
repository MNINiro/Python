# 9618_w21_41: 1
print("========Recursive Method===========")
def Unknown(X, Y):
    if X < Y:
        print(str(X + Y))
        return Unknown(X + 1, Y) * 2
    elif X == Y:
        return 1
    else:
        print(str(X + Y))
        return int(Unknown(X - 1, Y) / 2)


print("10 and 15")
print(Unknown(10, 15))
print()
print("10 and 10")
print(Unknown(10, 10))
print()
print("15 and 10")
print(Unknown(15, 10))

print("========Iterative Method===========")

def IterativeUnknown(X, Y):
    Total = 1
    while X != Y:
        print(str(X + Y))
        if X < Y:
            X = X + 1
            Total = Total * 2
        else:
            X = X - 1
            Total = int(Total / 2)
    return Total


print("10 and 15")
print(IterativeUnknown(10, 15))
print()
print("10 an 10")
print(IterativeUnknown(10, 10))
print()
print("15 and 10")
print(IterativeUnknown(15, 10))
