# Python program for Linear Search
# #create array to store all the numbers
myList = [4, 2, 8, 17, 9, 3, 7, 12, 34, 21]
# enter item to search for
item = int(input("Please enter item to be found "))
found = False
for index in range(len(myList)):
    if myList[index] == item:
        found = True
if found:
    print("Item found")
else:
    print("Item not found")
