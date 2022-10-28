from array import *


#
# # === Ex-1 === Passing array to a function
# def fun(ar):
#     print("Passed values in an array:", ar)
#     print("Array Type :", type(ar))
#     print()
#     for i in ar:
#         print(f"{i} in array")


# ===== Main body ======
# a = array('i', [101, 102, 103, 104])
# fun(a)

# === Ex-2 === Returning array from a function
# def func(ar):
#     print("Passed values in an array",ar)
#     print("Array Type :",type(ar))
#     for i in ar:
#         print(f"{i} in array")
#     return(ar)
#
# a = array('i', [101, 102, 103, 104])
# x = func(a)
# print("Returned values of the array",x)
# print(type(x))
# x.reverse() #reversing values of the array
# for i in x:
#     print(f"{i} from array")

# === Ex-3 === creating and Returning array from a function

def func():
    a = array('i', [101, 102, 103, 104])  # 'i' for integer
    return a


# === Many body ====
y = func()
print("Returned values of the array:", y)
print(type(y))

y.reverse()  # reversing values of the array (not necessary)
for i in y:
    print(f"{i} from array")
