#Ex-1: Nested Lambda function

add = lambda x = 10 : (lambda y: x + y)

#print(add()) #it will only show memory locations of the function
a = add() #here, a ia a function variable
print(a(20))

#Ex-2: Passing lambda function to another function

def show(a): # here, a is a function valiable which is executing the whole lambda function
    print('output of lambda :',a(8)) # a(8), argument 8 is passing to lambda's x variable.

show(lambda x : x)


#Ex-3: Retunting lambda function from a function

def add():
    y = 20
    return (lambda x : x + y) # function variable,a will pass argument 10 to lambda's x variable which will be added with y

a = add()
print('Result is ',a(10))

