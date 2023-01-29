lst = ['Janan', 'Rumaisa', 'Ayman', 'Sadman', 'Lamia']
length = len(lst)
found = False
searchItem = input('Enter a value to be searched:').lower()
#
# for i in range(length):
#     if searchItem == lst[i].lower():
#         print('Item found in position', i)
#         found = True
#
# if found == False:
#     print('Item does not exist')

# ==================================
for i in range(length):
    if searchItem == lst[i].lower():
        print('Item found in position', i)
        found = True

        print('ASCII values of', lst[i])
        for j in range(len(lst[i])):
            print(lst[i][j], ':', ord(lst[i][j]))
