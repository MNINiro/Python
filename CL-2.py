#List
# List name = [Value,value,value,......]
# L1 = [10,20,30,40]
# print(L1)
# print(L1[2] * L1[1])
# print()
#
# L2=['ID','Name','Class']
# L3=[101,'Masrur','XI']
# print()
#
# print(L2[0],'=',L3[0])
# print(L2[1],'=',L3[1])
# print(L2[2],'=',L3[2])
# print()
#
# NewList=[]
# print(NewList)
#
# NewList.append('aaa')
# print(NewList[0])
#
# L1.append(50)
# print(L1)
# print(len(L1))
#
# L2.append(L3)
# print(L2)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
print(b)
a.append(b)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])
print(a[3][2])
print()

a.extend(b)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(type(a[3]))

b[0]='Toyota'
print(b)

del b[0]
print(b)














