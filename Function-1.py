def add(arg1,arg2):      # Add both the parameters and return them.
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total

#======== main body ========

# x = int(input ('1st data :'))
# y = int(input ('2nd data :'))
#
# print('outside the function:',add(x,y)+10)

j = 100
add(add(10,10),j)
