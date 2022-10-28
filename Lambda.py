# Lambda or anonymous function
# It does not have any name to call
# lambda can take 0 or any number of arguments
# 'return' is not needed in lambda

# ===Example-1====
# sum = lambda x: x + 1
# print('Sum is', sum(15))  # 5 will pass to x

# #===Example-2====
# add = lambda x, y: x + y
# print("Total is:", add(5, 2))

# #===Example-3====
# show = lambda x: print('Output:', x / 2)
# show(50)

# #===Example-4====
# calc = lambda x, y: (x + y, x - y, x * y, x // y)
#
# i = int(input('Enter 1st data:'))
# j = int(input('Enter 2nd data:'))

# a, s, m, d = calc(i, j)

# print('Addition :', a)
# print('Subtraction:', s)
# print('Multiplication:', m)
# print('Division:', d)

# #===Example-5====
# mult = lambda x, y=3: x * y
# print('Multiplication:', mult(5))  # here, default value y=3 will be used

# #===Example-6====
# mult = lambda x=2, y=3: x * y
# print('Default:', mult())
# print('Overwritten:', mult(5, 6))  # here, default value x=5 will be used

# #===Example-7====
# mult = lambda x, y=3: x * y
# print('Mult:',mult(5,4)) # here, passed value 4 will replace default value y=3

# ===Example-8====

# The syntax of lambda functions contains only a single statement,
# which is as follows

# sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print("Value of total:", sum(10, 20))
