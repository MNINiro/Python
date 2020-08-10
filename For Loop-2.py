students=['protiva','niloy','jannat','armeen']

total = 0   #initialization
print(total)

for s in students:
    print(s,len(s))
    # total = total + len(s)
    total += len(s)
print('Total :', total)


