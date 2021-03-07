# reduce() works by calling the function we passed for the first two items in the sequence.
# The result returned by the function is used in another call to function alongside with the next (third in this case), element.

from functools import reduce

# #===Ex-1===
a = [10,20,30]

result= reduce(lambda n,m: n+m, a)
print(result)
print(type(result))

# #===Ex-2===
# def add(x, y):
#     return x + y
#
# list = [2, 4, 7, 3]
# print(reduce(add, list))

# #===Ex-3===
# list = [2, 4, 7, 3]
# x = reduce(lambda x, y: x + y, list)
# print('Initial reduced value:',x)
# print(type(x))
#
# y = str(reduce(lambda x, y: x + y, list, 10)) #10 will add with initial result, 16
# print("With an initial value: " + y)
# print(type(y))

# This process repeats until we've gone through all the elements in the sequence.
# The optional argument initial is used, when present, at the beginning of this
# "loop" with the first element in the first call to function. In a way, the initial element is the 0th element, before the first one, when provided.
# reduce() is a bit harder to understand than map() and filter(), so let's look at a step by step example:
# We start with a list [2, 4, 7, 3] and pass the add(x, y) function to reduce() alongside this list, without an initial value
# reduce() calls add(2, 4), and add() returns 6
# reduce() calls add(6, 7) (result of the previous call to add() and the next element in the list as parameters), and add() returns 13
# reduce() calls add(13, 3), and add() returns 16
# Since no more elements are left in the sequence, reduce() returns 16
# The only difference, if we had given an initial value would have been an additional step - 1.5. where reduce() would call add(initial, 2) and use that return value in step 2.
# Let's go ahead and use the reduce() function: