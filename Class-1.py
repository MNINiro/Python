Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 18%4
2
>>> 5*5*5
125
>>> 5**5
3125
>>> 5**3
125
>>> a=20
>>> 5+a
25
>>> b=20
>>> a+b
40
>>> a/b
1.0
>>> a//b
1
>>> a**b
104857600000000000000000000
>>> a-b
0
>>> b-a
0
>>> school is closed
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    school is closed
NameError: name 'school' is not defined
>>> 'school is closed
SyntaxError: EOL while scanning string literal
>>> 'school is closed'
'school is closed'
>>> 'i don't think so'
SyntaxError: invalid syntax
>>> "I don't think so"
"I don't think so"
>>> 'I don\'t think so'
"I don't think so"
>>> print("Hello World")
Hello World
>>> print('C:\Users\mnini\Desktop\Mazda
      
SyntaxError: EOL while scanning string literal
>>> print('C:\Users\mnini\Desktop\Mazda Pics')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> print('C:\Users\mnini\Desktop\MazdaPics')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> print('C:\Users\mnini\Desktop\MazdaPics')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
>>> \
  f
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    f
NameError: name 'f' is not defined
>>> firstName="MNI"
>>> lastName="Niro"
>>> firstName+lastName
'MNINiro'
>>> firstName*5
'MNIMNIMNIMNIMNI'
>>> firstName + lastName
'MNINiro'
>>> firstName + ' ' + lastName
'MNI Niro'
>>> firstName[2]
'I'
>>> firstName[0]
'M'
>>> firstName[-1]
'I'
>>> firstName[-2]
'N'
>>> firstName[-3]+firstName[-2]
'MN'
>>> lastName[1:2]
'i'
>>> lastName[1:3]
'ir'
>>> lastName[:4]
'Niro'
>>> lastName[:]
'Niro'
>>> len(firstName)
3
>>> len(lastName)
4
>>> len((firstName)+(lastName))
7
>>> List
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    List
NameError: name 'List' is not defined
>>> Team=[12,34,52,19,54]
>>> Team[3]
19
>>> Team[1]+Team[3]
53
>>> Team
[12, 34, 52, 19, 54]
>>> Team[2]=23
>>> team
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    team
NameError: name 'team' is not defined
>>> Team
[12, 34, 23, 19, 54]
>>> Team + [13,14,15]
[12, 34, 23, 19, 54, 13, 14, 15]
>>> Team
[12, 34, 23, 19, 54]
>>> Team.append(33)
>>> Team
[12, 34, 23, 19, 54, 33]
>>> Team[:2]
[12, 34]
>>> Team[:2]=[0,0]
>>> Team
[0, 0, 23, 19, 54, 33]
>>> Team[:2]-[]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    Team[:2]-[]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> eam[:2]=[]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    eam[:2]=[]
NameError: name 'eam' is not defined
>>> Team[:2]=[]
>>> Team
[23, 19, 54, 33]

