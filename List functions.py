
# - append(): Adds a single element to a list.
my_list = [1, 2, 3]
my_list.append(4)
print('Append:', my_list) # [1, 2, 3, 4]

'''
# - extend(): Adds multiple elements to a list.
my_list = [1, 2, 3]
my_list.extend([4, 5])
print('Extend:', my_list) # [1, 2, 3, 4, 5]


# - remove(): Removes the first item in the list with the specified value.
my_list = [1, 2, 3]
my_list.remove(2)
print('Remove:',my_list) # [1, 3]

# - del: Removes an item from a list given its index instead of its value.
my_list = [1, 2, 3]
del my_list[0]
print('Remove:', my_list) # [2, 3]

# - pop(): Removes the last item in the list or an indexed value from the list.
my_list = [1, 2, 3]
my_list.pop()
print('Pop:',my_list) # [1, 2]

my_list = [1, 2, 3]
my_list.pop(1)


# - reverse(): Reverses the list.
my_list = [1, 2, 3]
my_list.reverse()
print('Reverse:',my_list) # [3, 2, 1]

# - sort(): Sorts the list in ascending order.
my_list = [3, 1, 2]
my_list.sort()
print('Sort:',my_list) # [1, 2, 3]


# - clear(): Removes all items from the list.
my_list = [1, 2, 3]
my_list.clear()
print('Clear:',my_list) # []


# - count(): Returns the number of times a specified value appears in the list.
my_list = [1, 2, 3, 2]
print('Count:',my_list.count(2)) # 2


# - insert(): Inserts an element at a specified position in the list.
my_list = [1, 2, 3]
my_list.insert(1, 4)
print('Insert:',my_list) # [1, 4, 2, 3]


# - index(): Returns the index of the first occurrence of a specified value in the list.
my_list = [1, 2, 3]
print('Index:',my_list.index(2)) # value 2 in position 1


# - copy(): Returns a copy of the list.
my_list = [1, 2, 3]
new_list = my_list.copy()
print('Copy:',new_list) # [1, 2, 3]


# - len(): Returns the number of items in the list.
my_list = [1, 2, 3]
print('Length:',len(my_list)) # 3


# - min(): Returns the smallest item in the list.
my_list = [1, 2, 3]
print('Minimum:',min(my_list)) # 1


# - max(): Returns the largest item in the list.
my_list = [1, 2, 3]
print('Maximum:',max(my_list)) # 3
'''
