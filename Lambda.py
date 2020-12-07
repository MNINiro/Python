#Lambda or anonymous function
# It does not have any name to call
# lanbda can take 0 or any number of arguments
# 'return' is not needed in lambda

#===Example-1====
sum = lambda x: x + 1
print(sum(5)) # 5 will pass to x

#===Example-2====
add = lambda x,y: x + y
print("Total is:",add(5,2))

#===Example-3====
show = lambda x : print('Output:',x)
show(50)

#===Example-4====
add_sub = lambda x,y: (x+y, x-y)
a, s = add_sub(5,3)
print('Addition :',a)
print('Subtraction:',s)

#===Example-5====
mult = lambda x, y=3 : x * y
print(mult(5)) #here, default value y=3 will be used

#===Example-5====
mult = lambda x, y=3 : x * y
print(mult(5,4)) # here, passed value 4 will replace default value y=3





