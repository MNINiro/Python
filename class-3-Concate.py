Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a='Its a'
>>> b="Its b"
>>> c="""Its c"""
>>> print (a)
Its a
>>> print (b)
Its b
>>> print (c)
Its c
>>> d='Its d\'t'
>>> print (d)
Its d't
>>> b="Its a double \"qoutation"
>>> print (b)
Its a double "qoutation
>>> c="""Its a \triple \"quotation"""
>>> print (c)
Its a 	riple "quotation
>>> print (len(a))
5
>>> print (len(b))
23
>>> print (len(c))
23
>>> name="MNI"
>>> LName="Niro"
>>> print (name + LName)
MNINiro
>>> print (name * 3)
MNIMNIMNI
>>> print ((name + LName)*2)
MNINiroMNINiro
>>> a = 'Hello'
>>> b = 5
>>> print (a + b)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print (a + b)
TypeError: Can't convert 'int' object to str implicitly
>>> print (a + str(b))
Hello5
>>> 
