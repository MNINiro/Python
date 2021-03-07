from numpy import *

# #=== Ex-1 === Returning array from a function
def func(ar):
    print("Passed values in an array",ar)
    print("Array Type :",type(ar))
    for i in ar:
        print(f"{i} in array")
    return(ar)

print()
a = array([101, 102, 103, 104])
x = func(a)
print("Returned values of the array",x)
print(type(x))
for i in x:
    print(f"{i} from array")


# === Ex-2 === creating and Returning array from a function

# def func():
#     a = array([101, 102, 103, 104])
#     return a
#
# y = func()
# print("Returned values of the array",y)
# print(type(y))
# for i in y:
#     print(f"{i} from array")