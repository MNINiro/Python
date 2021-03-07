# a = 10
# b = 5
#
# print('Add :',a + b)
# print('Sub :',a - b)
# print('Multiplication :',a * b)
# print('Division :',a // b)
#
# c = 2.5
#
# print('Divide :',a / c)
#
# print('Addition :',2.5 + 2.5 + 2.5 + 2.5)
# print('Multiplication :',2.5 * 4)

def add(a, b):
    print('Result is', a + b)

def sub(a, b):
    print('Result is', a - b)

def mult(a, b):
    print('Result is', a * b)

def div(a, b):
    print('Result is', a / b)

# ==========Starting module==================

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
add(a, b)
sub(a, b)
mult(a, b)
div(a, b)

print("well done waasil " * 5)


