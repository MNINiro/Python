# Two or more methods have the same name but different
# numbers of parameters or different types of
# parameters, or both.
# These methods are called overloaded methods
# and this is called method overloading.

"""
# =========================================
# First product method.
# Takes two argument and print their
# product

def product(a, b):
    p = a * b
    print(p)


# product(4, 5)

# Second product method
# Takes three argument and print their
# product

def product(a, b, c):
    p = a * b * c
    print(p)


# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)
"""

"""
def add(a=None, b=None):
    # Checks if both parameters are available
    # if statment will be executed if only one parameter is available
    if a != None and b == None:
        print(a)
    # else will be executed if both are available and returns addition of two
    else:
        print(a + b)


# two arguments are passed, returns addition of two
add(2, 3)
# only one argument is passed, returns a
add(2)
"""


class greeting:
    def hello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")


myGreeting = greeting()
myGreeting.hello()
myGreeting.hello("Christopher")

