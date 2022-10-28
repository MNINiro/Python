#=== Ex-1 ===
# b = [10,20]
# a = [1,2,3,4,b]
# print(a)


# === Ex-2 ===same output
a = [11,22,33,44,[10,20]]
print('Original list:',a)
# print("Wrong output",a[3][1]) #it will show an error since 3rd element does not have any sublist
print('Valid output:',a[3])
print('List with a sublist:',a[4][1])

# a.append(5)
# print("After append:",a)
#
# a[4][1] = 55 #inside sublist
# print(a)

L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

for list in L:
    print(list)

    total = 0
    for number in list:
        total += number
    print(total)

# #=== Ex-3 ===
# c = [[10,20,30],[40,50,60]]
# print('Full List',c)
# print('1st sub list:',c[0])
# print('2nd sub list:',c[1])
# print('First sublist element:',c[0][1])
# print('Second sublist element:',c[1][1])

# x = len(c[0])
# y = len(c[1])
# print(x,' ',y)


#=== Ex-4 ===
# c = [[10,20,30],[40,50,60]]
# i = 0
# while i < len(c[0]):
#     j = 0
#     while j < len(c[1]):
#         print(f'in i {i} and in j {j}:',c[i][j])
#         j += 1
#     i += 1


# #=== Ex-5 ===
# c = [10,20,30,[50,60]]
# n = len(c) #4 (0 to 3)
#
# for i in range(n):
#     if type(c[i]) is list: #False since c[i] is an Integer, until c[i] = 3, which is a list [50,60]
#         if len(c[i]) > 1:  #if multiple elements in a list, here, which is true
#             m = len(c[i])  # m = 2
#             for j in range(m):
#                 print(i,j, c[i][j])
#     else:
#         print(i, c[i])


# #=== Ex-6 ===
# a = [[10,20,30],[50,60]]
#
# for r in a:     # Here, r is first element in 0 index that is [10,20,30]. Then index 1, [50,60]
#     for c in r: # to read each element of r, another loop c is used
#         print(c)
#     print()


# #=== Ex-7 ===
# a = [[10,20,30],[50,60]]
# n = len(a)
#
# for i in range(n):              # i = 0, [10,20,30]. i = 1, [50,60]
#     for j in range(len(a[i])):  # Here, it will read each element of each sublist
#         print(i, j, a[i][j])
#     print()

# #=== Ex-8 ===
# a = [[10,20,30],[50,60]]
# n = len(a)
# i = 0
# while i < n:
#     if type(a[i]) is list:  # False since a[i] is an Integer, until a[i] = 2, which is a list [50,60]
#         if len(a[i]) > 1:  #if multiple elements in a list, here, which is true
#             j = 0
#             m = len(a[i])  # m = 2
#             while j < m:
#                 print(i,j,a[i][j])
#                 j += 1
#             i += 1
#     else:
#         print(i,a[i])
#         i += 1


# # #=== Ex-9 ===
# a = [[10,20,30],[50,60]]
# n = len(a)
# i = 0
# while i < n:
#     j = 0
#     while j < len(a[i]):
#         print(i, j, a[i][j])
#         j += 1
#     i += 1

