x = []
print(x)

x.append(10)
x.append(25)
print(x)

y = x[0] + x[1]
print(y)

x.append(y)

print(x[0])
print(x[1])
print(x[2])

names=["Adib","Shabab","Fuad"]
days=["sun","mon","tue","wed"]

print(names)
print(days)
print(names[1] +' plays on '+ days[2])

print(len(names))
print(len(days))

print(len(names[0]))

names.append("Karim")
print(names)

age=[23,20,18,20]
# names.append(age)
# print(names)

names.extend(age)
print(names)

print (len(names))
print (len(names[2]))
#
# i = "sdjhfhdshbr4546456fghf"
# print(len(i))
