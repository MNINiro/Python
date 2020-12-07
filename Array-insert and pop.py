from array import *

studentRoll = array('i',[101,102,103,104,105])
ln = len(studentRoll)
i = 0
while (i < ln):
    print('in',i, 'position:', studentRoll[i])
    i += 1

print("Array after insert new elements")

studentRoll.insert(1,106) # after inserting 106 in position 1, existing position 1's element will move to position 2
studentRoll.insert(4,107) # 107 will be inserter according to the updated current position.

ln = len(studentRoll)
i = 0
while (i < ln):
    print('in',i, 'position:', studentRoll[i])
    i += 1

# print("==== pop an element from existing array ====")
#
# studentRoll.pop()   # it will pop an element from the last position of an array
# studentRoll.pop(3) # it will remove the 3rd position element of the array. Rest of the elements positions will be updated
# ln = len(studentRoll)
# i = 0
# while (i < ln):
#     print('in',i, 'position:', studentRoll[i])
#     i += 1


print("==== remove specific element from existing array ====")

studentRoll = array('i',[101,106,103,104,106])

studentRoll.remove(106)     # it will remove only one specific element from the beginning of the array.
# studentRoll.remove(105)     # it will show value error if the element is not in the array

ln = len(studentRoll)
i = 0
while (i < ln):
    print('in',i, 'position:', studentRoll[i])
    i += 1
