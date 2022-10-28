# === Ex-1 ===
# def add(*num):
#     z = num[0] + num[1] + num[2]
#     return z
#
#
# print('Add:', add(12, 13, 14))
# print("sum is:", add(5, 2, 4))


# Ex-2
# def add(a, b, *num):
#     z = num[0] + num[1]
#     return z + (a + b)


# print(add(5, 5, 12, 13))

# === Ex-3 ===
# def add1(x, *num):
#     z = x + num[0] + num[1]
#     return z


# t = add1(12, 12, 6)  # first element will pass to x and rest to *num
# print('t:', t)
# print("sum is:", add1(t, 5, 2, 6, 5))  # it will not show an error even it is passing more elements than the number
# of indices


# #=== Ex-4 === Keyword variable
def add2(**num):
    z = num['a'] + num['b'] + num['c']
    return z


print(add2(c=20, b=30, a=10))
# print("sum is:", add2(a=5, b=2, c=6, d=5))


# === Ex-5 === Keyword variable
def add3(y, **num):
    z = y + num['a'] + num['b'] + num['c']
    print(z)
    return z


add3(10, a=12, b=12, c=12)  # first element will pass to y and rest to **num
# print("sum is:", add3(20, a=5, b=2, c=6, d=5))  # it will not show an error even it is passing the value of d
