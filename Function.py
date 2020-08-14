def add(arg1, arg2):      # Add both the parameters and return them.

    total = arg1 + arg2
    print("Inside the function : ", total)
    # return total;
 

def sub(arg1, arg2):      # Add both the parameters and return them.

    total = arg1 - arg2
    print("Inside the function : ", total)
    # x = add(4, 4) + total
    # print("Temporary:",x)
    # return total;

## ======== Main Body ==================
##
# add(10,15)
##
x = int(input('Enter 1st Data :'))
y = int(input('Enter 2nd Data :'))

add(x,y)

sub(x,y)

z = x+y

add(z,x)


#print("Outside the function :",add(10,20)+50)

# print("Outside the function :",sub(20,15)+50)

#print("Outside the function :",add(10,20)+ sub(15,5)+50)
