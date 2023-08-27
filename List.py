# The most basic data structure in Python is the sequence. Each element of a
# sequence is assigned a number - its position or index. The first index is zero,
# the second index is one, and so forth.
# Python has six built-in types of sequences, but the most common ones are lists
# and tuples
# '''
# lst = []
# list1 = ["physics", 'chemistry', 1997, 20.50, True]
# list2 = [1, 2, 3, 4, 5, 6, 7]

# print(list1)
# print ("list1: ", list1[3])

# print ("list2: ", list2[3:6])
#
# print ("list2: ", list2[-3:-1])
# '''


# Updating Lists # uncomment following code for execution
list3 = ['physics', 'chemistry', 1997, 2000]
# print ("Value available at index 2 : ")
# print (list3[2])

# list3[2] = 2001;
# print ("New value available at index 2 : ")
# # print (list3[2])
# print(list3)

'''
# Delete List Elements # uncomment following code for execution
list1 = ['physics', 'chemistry', 1997, 2000];
print(list1)
del list1[1];
print("After deleting value at index 1 : ")
print(list1)
'''

# '''
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

# list1.append("Bangla")
# print(list1)

# list1.append(list2)
# print('Append:', list1)
# print()
# print('Length:',len(list1))
# print(list1[4][3])

list1.extend(list2)
print(list1)

#
# for i in range(len(list1)):
#     print('item no',i,':', list1[i])
#



list1.clear()
print(list1)

# print()
# list1.append(list2)
# print(list1)
# '''
