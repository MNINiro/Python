# A tuple is a sequence of immutable Python objects. Tuples are sequences,
# just like lists. The differences between tuples and lists are, the tuples
# cannot be changed unlike lists and tuples use parentheses, whereas lists use
# square brackets.
List1 = ['physics', 'chemistry', 19.97, 2000, True, '25-10-2001']
tup1 = ('physics', 'chemistry', 19.97, 2000, False, '25-10-2001')
print(List1)
print(tup1)
print()
#
print("tup1-1: ", tup1[1], type(tup1[1]));
print("tup1-2: ", tup1[2], type(tup1[2]));
print("tup1-3: ", tup1[3], type(tup1[3]));
print("tup1-4: ", tup1[4], type(tup1[4]));
print("tup1-5: ", tup1[5], type(tup1[5]));

print(type(List1))
print(type(tup1))
print()

# tup2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# total = 0
# for i in range(0,10,3):
#     print ("tup2 :", tup2[i])
#     total += tup2[i]
#
# print('Total:', total)
#
# i = 1   #position
# total = 0
# while(i < len(tup2)):
#    print ("tup2 :", tup2[i]); #value of the iTH position
#    total += tup2[i]     # Totalling
#    i += 2               # counter
# print('Total:', total)

# Updating Tuples
tup1 = (12, 34.56);
print(type(tup1))
print(tup1)
tup2 = ('abc', 'xyz');
print(tup2)

# Following action is not valid for tuples
# tup1[0] = 100;
# print(tup1)

# # So let's create a new tuple as follows
# tup4 = (100,200);
# print(tup4)

# like extends of list
# tup3 = tup1 + tup2;
# print(tup3);
# print(type(tup3));
# print(len(tup3))

# Delete Tuple Elements

# tup = ('physics', 'chemistry', 1997, 2000)
# print(tup)
#
# del tup[2]
# print("After deleting tup : ");
# print(tup);
