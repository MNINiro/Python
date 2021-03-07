# def add():
#     x = int(input('Enter 1st data:'))
#     y = int(input('Enter 2nd data:'))
#     z = x+y
#     print(f'Addition is {z}')
#
# for i in range(3):
#     add()
#============================
def add1(arg1,arg2):      # Add both the parameters and return them.
    total = arg1 + arg2
    print("Addition inside the function :", total)
    return total

def sub1(arg1,arg2):      # Add both the parameters and return them.
    total = arg1 - arg2
    print("Subtraction inside the function :", total)
    return total

# ======== main body ========

x = int(input ('1st data :'))
y = int(input ('2nd data :'))

# add1(x,y)
sub1(x+10,y+5)
print('outside the function:',add1(x,y)+10)

j = 100
add1(add1(10,10),j) #Inner add1 will execute first then outer add1
