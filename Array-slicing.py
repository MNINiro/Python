from array import *

studentRoll = array('i', [101, 102, 103, 104, 105])

# sl = studentRoll[1:4]  # sliced elements from original array. [:2], [1:], [:],[-3:],[-5:-3] etc can be used

sl = studentRoll[-5:-3]
for i in sl:
    print(i)
