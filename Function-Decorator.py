# Functlon Decorator
# A Decorator function is a function that accepts a function as parameter and returns a function.
# A decorator takes the result of a function, modifies the result and returns it.
# In Decorators, functions are taken as the argument into another function and
# then called inside the wrapper function.
# We use @function_name to specify a decorator to be applied on another
# function.

#===Ex-1===without decor
def decor(func): #2, directly go to return
    def inner(): #4
        print("Inner function: Before enhancing") #5
        func() #6, here func = num, so control will be given to num
        print("Inner function: After enhancing") #10, after num, code will return control here
    return inner() #3, now calling inner after visiting result

def num(): #7, now num will execute
    print("We will use this function") #8
    print("and will enhance this with decorator") #9

result = decor(num) #1 calling decor and passing num to func, #7 func=num, therefore, result = num

# #===Ex-2===with decor
# def decor(num): #2
#     def inner(): #4
#         print("IF: Before enhancing") #5
#         num() #6
#         print("IF: After enhancing") #10
#     return inner() #3
#
# @decor
# def num(): #7
#     print("We will use this function") #8
#     print("and will enhance this with decorator") #9
#
# num #1

# #===Ex-3===without decor
# def decor(fun): #2
#     def inner(): #4
#         a = fun() #5, here, a=10 from num
#         add = a + 5 #8, add=15
#         return add #9
#     return inner() #3
#
# #to enhance following num function we are creating "def decor()" function
# def num(): #6 num = fun
#     return 10 #7
#
# result = decor(num) #1, 10, now pass the result 15 to result
# print("Result is",result), #11


#===Ex-4===with decor
# def decor1(num): #2
#     def inner(): #4
#         a = num() #5, here, a=10
#         add = a + 5 #8, add=15
#         return add #9
#     return inner() #3
#
# #to enhance following num function we are creating "def decor()" function
# @decor1
# def num(): #6 num = fun
#     return 10 #7. This is the original value
#
# print("Result is",num), # 1, 10

# #===Ex-5===without decor
# def decor1(num): #2
#     def inner():
#         b = num()#10
#         mult = b * 5 #12
#         return mult #13
#     return inner #3
#
# def decor(num): #
#     def inner(): #5
#         a = num() #9,14
#         add = a + 5 #15
#         return add #16
#     return inner #6
#
# def num():#11
#     return 10 #11
#
# num = decor(decor1(num)) #1,4,7,12
# print("The final value is",num())#8,17


# #===Ex-5===with decor
# def decor1(num): #
#     def inner():
#         b = num()#10
#         mult = b * 5 #12
#         return mult #13
#     return inner #3
#
# def decor(num): #
#     def inner(): #5
#         a = num() #9,14
#         add = a + 5 #15
#         return add #16
#     return inner #6
#
# @decor
# @decor1
# def num():#
#     return 10 #
#
# print(num())