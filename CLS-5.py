lst = [12, 56, 23, 78, 45, 56, 33, 55, 88]

ln = len(lst)
# print("Length:", ln)
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])

total = 0
for i in range(ln):
    print(i,":", lst[i])
    total = total + lst[i]
    print('Total:', total)

# print('===========================')
#
# total = 0
# for i in lst:
#     # print(i)
#     total = total + i
# print('Total:', total)



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
