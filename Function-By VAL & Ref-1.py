##An asterisk (*) is placed before the variable name that holds the values of
##all nonkeyword variable arguments. This tuple remains empty if no additional
##arguments are specified during the function call. Following is a simple example 

# Function definition is here

def printinfo(arg1, *num):
    total = arg1
    count = 1

    for i in num:
        total += i
        count += 1

    print('Total :', total)
    print('No of items:', count)
    return


printinfo(70, 60, 50, 40)
