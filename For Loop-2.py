students=['Ayman','Darras','jannat','armeen']

total = 0   #initialization

for s in students:
    print(s,'length:',len(s))
    # total = total + len(s)
    total += len(s)

print('Total :', total)


