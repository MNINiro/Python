LTSD = [1,2,3,(10,20,30),{101,202,303},{'x':50, 'y':75}]

print('List:')
for i in LTSD:
    print(i)                #will print first 3 LIST elements

    if i == 3:              #will print TUPLE elements
        print("\nTuple:")
        for j in LTSD[3]:
            print(j)

        i += 1               #increasing the value of i since loop ends in the previous statemt

    if i == 4:              #will print SET elements
        print("\nSet:")
        for k in LTSD[4]:
            print(k)

        i += 1

    if i == 5:              #Will print DICTIONARY elements
        print('\nDictionary:')
        for key,value in LTSD[5].items():
            print(key,'=',value)
        break   #so, loop will terminate here with the existing i=3 value

# print('\nCalculation:',LTSD[1] + LTSD[3][1] + LTSD[4].pop() + LTSD[5]['x'])
