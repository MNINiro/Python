import array as ar

print('========= example-1 === for Loop ==========')

studentRoll = ar.array('i',[101,102,103,104,105]) # 'i' for integer

for x in studentRoll: #does not need to define length of the array/list etc.
    print(x)    #to read data directly

print('========= example-2 === for Loop ==========')

ln = len(studentRoll)
for y in range(ln):
    print('in',y, 'position:', studentRoll[y]) #to read data from a certain position

print('========= example-3 === While Loop ==========')

z = 0
while (z < ln):
    print('in',z, 'position:', studentRoll[z])
    z += 1

print('========= example-4 === append in array ==========')

studentRoll.append(106)     #new element has been appended
studentRoll.append(107)     #new element has been appended
print(studentRoll)
print(type(studentRoll))

ln = len(studentRoll)       #len must be recalculated
z = 0
while (z < ln):
    print('in',z, 'position:', studentRoll[z])
    z += 1

print('========= example-5 === append in array by user input ==========')

from array import *
studentRoll = array('i',[])
n = int(input("How many elements :"))

for i in range(n):
    studentRoll.append(int(input("Enter only integer to append in the array :")))

print(studentRoll)

for i in range(n):
    print('in',i, 'position:', studentRoll[i])

print('========= example-6 === append in array by user input ==========')

i = 0
j = 0

while i < n:
    studentRoll.append(int(input("Enter only integer to append in the array  :")))
    i += 1
studentRoll.append(10)
studentRoll.append(20)

ln = len(studentRoll) # new length has been created after entering elements in the array
while j < ln:
    print('in', j, 'position:', studentRoll[j])
    j += 1

print(studentRoll)