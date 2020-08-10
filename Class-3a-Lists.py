Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> names=["AAA","BBB","CCC"]
>>> names
['AAA', 'BBB', 'CCC']
>>> names[0]
'AAA'
>>> names[2]
'CCC'
>>> days=["sun","mon","tue"]
>>> days
['sun', 'mon', 'tue']
>>> days[2]
'tue'
>>> print (names[1] + days[2])
BBBtue
>>> days[-1]
'tue'
>>> names[-2]
'BBB'
>>> print (len(names[0]))
3
>>> print (Names[-1] + days[0])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print (Names[-1] + days[0])
NameError: name 'Names' is not defined
>>> print (names[-1] + days[0])
CCCsun
>>> 
>>> 
>>> names.a
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    names.a
AttributeError: 'list' object has no attribute 'a'
>>> names.append("DDD")
>>> names[3]
'DDD'
>>> names
['AAA', 'BBB', 'CCC', 'DDD']
>>> age=[23,20,18]
>>> age
[23, 20, 18]
>>> names.extend(age)
>>> names
['AAA', 'BBB', 'CCC', 'DDD', 23, 20, 18]
>>> "remove item from list"
'remove item from list'
>>> names.remove("BBB")
>>> names
['AAA', 'CCC', 'DDD', 23, 20, 18]
>>> 
>>> print (names,age)
['AAA', 'CCC', 'DDD', 23, 20, 18] [23, 20, 18]
>>> print (names,age,days)
['AAA', 'CCC', 'DDD', 23, 20, 18] [23, 20, 18] ['sun', 'mon', 'tue']
>>> len(names)
6
>>> len(names,age,days)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    len(names,age,days)
TypeError: len() takes exactly one argument (3 given)
>>> max(age)
23
>>> max(names)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    max(names)
TypeError: unorderable types: int() > str()
>>> 
