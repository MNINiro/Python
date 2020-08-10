# A tuple is a sequence of immutable Python objects. Tuples are sequences,
# just like lists. The differences between tuples and lists are, the tuples
# cannot be changed unlike lists and tuples use parentheses, whereas lists use
# square brackets.

# tup1 = ('physics', 'chemistry', 1997, 2000)
#
# print ("tup1-1: ", tup1[1])
# print ("tup1-3: ", tup1[3])

# tup2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 );
# total = 0
#
# for i in range(7):
#     print ("tup2 :", tup2[i]);
#     total += tup2[i]
# print('Total:', total)


# i = 1
# total = 0
#
# while(i < len(tup2)):
#    print ("tup2 :", tup2[i]);
#    total += tup2[i]     # Totalling
#    i += 2               # counter
# print('Total:', total)



# Updating Tuples

# tup1 = (12, 34.56);
#
# tup2 = ('abc', 'xyz');

# Following action is not valid for tuples

# tup1[0] = 100;
# print(tup1)

# # So let's create a new tuple as follows

# tup4 = (100,200);
# print(tup4)

# tup3 = tup1 + tup2;
# print (tup3);



#Delete Tuple Elements

tup = ('physics', 'chemistry', 1997, 2000);
print (tup);

del tup[2];

print ("After deleting tup : ");
print (tup);




