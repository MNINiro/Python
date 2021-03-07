from array import *

studentRoll = array('i',[101,102,103,104,105])
print("Position of the element in the array is",studentRoll.index(103)) #it will return the position of the array

print("==== Elements in the array ====")

ln = len(studentRoll)
i = 0
while (i < ln):
    print('in',i, 'position:', studentRoll[i])
    i += 1

print("==== After reverse ====")

studentRoll.reverse() # all elements will be reversed but not positions
i = 0
while (i < ln):
    print('in',i, 'position:', studentRoll[i])
    i += 1


print("==== extend method in array ====")

NewStudentsRoll = array('i',[201,202,203])
studentRoll.extend(NewStudentsRoll)
ln = len(studentRoll)
i = 0
while (i < ln):
    print('in',i, 'position:', studentRoll[i])
    i += 1
