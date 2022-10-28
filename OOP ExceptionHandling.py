# import module sys to get the type of exception
import sys

# Ex-1
randomList = ['a', 0, 2]

# for i in randomList:
#     try:
#         print("The entry is", i)
#         r = 1/int(i)
#         break
#     except:
#         print("Oops!", sys.exc_info()[0], "occurred.")
#         print("Next entry.")
#         print()
# print("The reciprocal of", i, "is", r)

# Ex-2-program to print the reciprocal of even numbers

# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 100/num
#     print("reciprocal: ",reciprocal)

# Ex-3- define a function to divide two numbers
# def division(a, b):
#     # use the try statement where error may occur
#     try:
#         print(a/b)
#     # if the error occurs, handle it !!
#     except ZeroDivisionError:
#         print("Cannot divide by Zero!!")
#     else:
#         print("No Error occured!!")
#     finally:
#         print('Value of a =', a, 'and b =', b)
#
# division(10,0)
# # print()
# division(10,2)

# Ex-4- Multiple catch
import math

def square(x):
    if int(x) == 0:
        raise ValueError('Input argument cannot be zero')
    if int(x) < 0:
        raise TypeError('Input argument must be positive integer')
    return math.pow(int(x), 2)

while True:
    try:
        y = square(input('Please enter a number: \n'))
        print(y)
    except ValueError as ve:
        print(type(ve), '::', ve)
    except TypeError as te:
        print(type(te), '::', te)
    # finally:
    #     x = y
    #     if x > 0:
    #         break
