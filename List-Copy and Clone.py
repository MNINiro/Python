a = [1,2,3,4]
b = a.copy() # a and b will be two independent list
print(a)
print(b)

print("Modifying a")
a[1] = 10
print("list a:",a)
print("list b:",b)

print("Modifying b")
b[2] = 55
print("list a:",a)
print("list b:",b)
