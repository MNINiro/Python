# In Call by value method original value is not modified whereas,
# in Call by reference method, the original value is modified.
# In Call by value, a copy of the variable is passed whereas in
# Call by reference, a variable itself is passed.
#==============================================================
# Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”.
# In the event that you pass arguments like whole numbers, strings or tuples to a function,
# the passing is like call-by-value because you can not change the value of the immutable objects
# being passed to the function. Whereas passing mutable objects can be considered as call by reference
# because when their values are changed inside the function, then it will also be reflected outside
# the function.


# call by value
string = "Geeks"

def test(string):
    string = "InCIS Ltd."
    print("Inside Function:", string) # No changes


# Driver's code
test(string)
print("Outside Function:", string)
print()

#========================================

# call by reference
def add_more(list):
    list.append(50)
    print("Inside Function", list)


# Driver's code
mylist = [10, 20, 30, 40]

add_more(mylist)
print("Outside Function:", mylist) # List changed