from array import *

studentRoll = array('i',[101,102,103,104,105])

sl = studentRoll[1:3] #sliced elements from original array. [:2], [1:], [:],[-3:],[-5:-3] etc can be used

for i in sl:
    print(i)

