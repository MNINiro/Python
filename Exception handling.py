# Example-1:
NumberString = input("enter an integer : ")
try:
    n = int(NumberString)
    print(n)

except:
    print(" This was not an integer")


# Example-2:
# a = [1, 2, 3]
# try:
#     print("Second element = %d" % (a[1]))
#
#     # Throws error since there are only 3 elements in array
#     print("Fourth element = %d" % (a[3]))
#
# except:
#     print("An error occurred")


# Example-3:
'''
def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
'''

"""
# Example-4:
def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


# Driver program to test above function
# AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
"""

"""
# Example-5:
# Python program to demonstrate finally

# No exception Exception raised in try block
try:
    k = 5 // 0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
# """