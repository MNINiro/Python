# Python program for finding an item in a linked list
myLinkedList = [27, 19, 36, 42, 16, None, None, None, None, None, None, None]
myLinkedListPointers = [-1, 0, 1, 2, 3, 6, 7, 8, 9, 10, 11, -1]
startPointer = 4
nullPointer = -1
heapStartPointer = 0
itemAdd = 0
tempPointer = 0

def find(itemSearch):
    found = False
    itemPointer = startPointer
    while itemPointer != nullPointer and not found:
        if myLinkedList[itemPointer] == itemSearch:
            found = True
        else:
            itemPointer = myLinkedListPointers[itemPointer]
    return itemPointer


# enter item to search for
# item = int(input("Please enter item to be found "))
# result = find(item)
# if result != -1:
#     print("Item found")
# else:
#     print("Item not found")
#
# find(42)


# Inserting items into a linked list
def insert(itemAdd):
    global startPointer, tempPointer

    if heapStartPointer == nullPointer:
        print("Linked List full")
    else:
        tempPointer = startPointer
        startPointer = heapStartPointer


heapStartPointer = myLinkedListPointers[heapStartPointer]
myLinkedList[startPointer] = itemAdd
myLinkedListPointers[startPointer] = tempPointer

insert(111)

# ======== Deleting items from a linked list =========
def delete(itemDelete):
    global startPointer, heapStartPointer
    if startPointer == nullPointer:
        print("Linked List empty")
    else:
        index = startPointer
        while myLinkedList[index] != itemDelete and index != nullPointer:
            oldindex = index
            index = myLinkedListPointers[index]
        if index == nullPointer:
            print("Item ", itemDelete, " not found")
        else:
            myLinkedList[index] = None
            tempPointer = myLinkedListPointers[index]
            myLinkedListPointers[index] = heapStartPointer
            heapStartPointer = index
            myLinkedListPointers[oldindex] = tempPointer

delete(16)