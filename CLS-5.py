lst = [12, 56, 23, 78, 45, 56, 33, 55, 88]

x = len(lst)

total = 0
for i in range(x):
    total = total + lst[i]
print('Total:', total)

print('===========================')

total = 0
for i in lst:
    # print(i)
    total = total + i
print('Total:', total)



# for i in range(10):
#     print(i * 2)


# lst = [1, 4, 2, 5, 7, 8, 9, 0, 3]
#
# for i in range(len(lst)):
#     print(lst[i])
#
# print('============')
# tup = {23, 67, 3453, 'gh'}
# for i in tup:
#     print(i)
