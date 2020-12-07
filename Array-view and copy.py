from numpy import *

a = array([10,20,30,40])
b = a.view()
print(a)
print(b)

print('a', id(a))
print('b', id(b))

#=============================

a = array([10,20,30,40])
b = a.copy()
print(a)
print(b)

print('a', id(a))
print('b', id(b))
