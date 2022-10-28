##Keyword arguments

##Keyword arguments are related to the function calls.
##When you use keyword arguments in a function call, the caller identifies
##the arguments by the parameter name.

# Function definition is here

# def printStr(st, tt):  # there are two arguments
#     # "This prints a passed string into this function"
#     print(st, tt)  # Normal output
#     print(f'first name is', st, 'and the Last name is', tt)
#     x = st, tt  # converted into a tuple
#     print(x)
#     return
#
#
# # ========== Now you can call printme function ===========
# fst = "Tahmeed"
# lst = "Ahmed"
# printStr(fst, lst)

##printStr( str = "Hello World!")

# ======================================
# def printinfo(name, age):
#     # "This prints a passed info into this function"
#     print("Name: ", name)
#
#     if (int(age) > 120) or (int(age) < 0):
#         print('Invalid age')
#     else:
#         print("Age ", age)
# return


# ====================================
# Now you can call printinfo function
# printinfo(50, "miki")
# printinfo("miki", 50)
# printinfo(age=55, name="Miki")

# ======================================

# Default arguments

##Function definition is here

def printinfo(name='Masrur', age=35):     # default values
    print("Name: ", name)
    print("Age ", age)
    print(f'name is {name} and the age is {age}')
    return

# Now you can call printinfo function
printinfo(name="Miki")
printinfo()
# print()
# printinfo(age=50, name="miki" )
# print()
# printinfo()
