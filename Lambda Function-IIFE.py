#Immediately Invoked Function Expression (IIFE)
# This function does not need to be called

#Ex-1:
# sum = lambda x: x + 10
# print(sum(5))

#Ex-1 IIFE:
lambda x: print(x + 10)(5)  # argument 5 will pass to lambda's x parameter

#Ex-2:
# add = lambda x,y: x + y
# print(add(5, 7))

# #Ex-2 IIFE:
lambda x, y: print(x + y)(5, 7)  # argument 5 and 6 will pass to lambda's x and y parameter

