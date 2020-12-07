#Immediately Invoked Function Expression (IIFE)
# This function does not need to be called

#Ex-1:
sum = lambda x : x + 10
print(sum(5))

#Ex-2:
(lambda x : print(x + 1)) (5) #argument 5 will pass to lambda's x parameter

#Ex-3:
add = lambda x,y : x + y
print(add(5,7))

#Ex-4:
(lambda x,y : print(x + y)) (5,6) #argument 5 and 6 will pass to lambda's x and y parameter

