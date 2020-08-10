Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myList=[0,1,2,3,4,5,6,7,8,9]
>>> myList
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> myList[4:7]
[4, 5, 6]
>>> myList[5:9]
[5, 6, 7, 8]
>>> myList[9:0]
[]
>>> FL=myList[0:2]
>>> LL=myList[3:7]
>>> print (FL + LL)
[0, 1, 3, 4, 5, 6]
>>> FL
[0, 1]
>>> FL[1]
1
>>> print (FL[1] + LL[2])
6
>>> FL
[0, 1]
>>> LL
[3, 4, 5, 6]
>>> names['a','b','c','d']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    names['a','b','c','d']
NameError: name 'names' is not defined
>>> names=['a','b','c','d']
>>> names[1:3]
['b', 'c']
>>> print (names[2] + names[0])
ca
>>> names[1:]
['b', 'c', 'd']
>>> names[:4]
['a', 'b', 'c', 'd']
>>> names[-4:-2]
['a', 'b']
>>> myList[-6:-2]
[4, 5, 6, 7]
>>> myList[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> myList[-1]
9
>>> myList[-2]
8
>>> names[-1:-3]
[]
>>> names[-5:-1]
['a', 'b', 'c']
>>> myList[-5:-1]
[5, 6, 7, 8]
>>> myList[-5:1]
[]
>>> skip some values from a list
SyntaxError: invalid syntax
>>> myList[0:10:2]
[0, 2, 4, 6, 8]
>>> myList[0:10:3]
[0, 3, 6, 9]
>>> myList[::2]
[0, 2, 4, 6, 8]
>>> myList[::-2]
[9, 7, 5, 3, 1]
>>> 
