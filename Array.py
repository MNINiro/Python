# print('========= example-1 ==========')
import array as a
studentRoll = a.array('i',[101,102,103,104,105]) # 'i' for integer
# studentRoll = [101,102,103,104,105] # it's a list

# print(studentRoll[0])
# print(studentRoll[1])
# print(studentRoll[2])
# print(studentRoll[3])
# print(studentRoll[4])

for i in range(5):
    print(studentRoll[i])

# print('========= example-2 ==========')
from array import *
studentRoll = array('f',[10.1,30,10.3,20,34.5]) #'f' for float. float also contains integer

print(studentRoll[0])
print(studentRoll[1])
print(studentRoll[2])
print(studentRoll[3])
print(studentRoll[4])

