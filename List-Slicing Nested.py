x = [[10,20,30],[40,50,60],[70,80,90,100],[11,22,33],[44,55,66],[77,88,99],[12,13,14]]
print("orginal list :",x)
print()

print("from 1st to 4th position")
a = x[1:5]
print(a)
print()

print("from 0th to last position")
a = x[0:]
print(a)
print()

print("from 1st to 4th position")
a = x[1:5]
print(a)
print()

print("from 0 to 4th position")
a = x[:5]
print(a)
print()

print("from 4th to last position")
a = x[4:]
print(a)
print()

print("Reverse from 0 to 5th position")
a = x[:-5]
print(a)
print()

print("Last 5 lists [-5-(-3)]=2 lists towards right")
a = x[-5:-3]
print(a)
print()

print("from 0th 1 position to the last position")
a = x[0][1:] #from 1st element to the last element of the oth index.
print(a)
print()

print("Slicing 2nd list")
a = x[2:4][1]
print(a)
print()

print("Slicing 2nd list")
a = x[2:3][0][1:4]
print(a)
print()

print("Slicing nested 2nd position, 0th position")
a = x[2:3]
print(a)
b = x[2:3][0]
print(b)
print()

print("Slicing 2nd list then extract elements")
a = x[2:3][0][0]
print(a) #it will print only the first element,70
i = x[2:3][0] #It is the sublist of the 2nd position
for el in i:
    print(el)
print()

print("Last nested 4 lists then 1st position then extract elements")
a = x[-4:][1][0]
print(a) #it will print last 4 sublists
i = x[-4:][1] #these are the elements of the 1st sublist of the extracted list [44,55,66]
for el in i:
    print(el)
print()