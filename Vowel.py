Stns = "I have a Dell Laptop, whats about you"
Stns = Stns.upper()
print(Stns)
x = len(Stns)
print('Charecters:',x)
a = 0
e = 0
i = 0
o = 0
u = 0
for j in range(x):
    if Stns[j] == "A":
        a += 1
    elif Stns[j] == "E":
        e += 1
    elif Stns[j] == "I":
        i += 1
    elif Stns[j] == "O":
        o += 1
    elif Stns[j] == "U":
        u += 1
print("a :",a)
print("e :",e)
print("i :",i)
print("o :",o)
print("u :",u)
      
    
