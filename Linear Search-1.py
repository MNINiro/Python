def forloop(list,searchItem):
    found = 0  # initially it is false

    for i in range(len(list)):
        if searchItem == list[i]:
            found = 1
            print('item found', searchItem, 'in position:', i)
    if found == 0:
        print('item not found')

# ============================

def whileloop(list, searchItem):
    found = False  # initially it is false
    i = 0
    while i < (len(list)):
        if searchItem == list[i]:
            found = True
            print("Item found", searchItem, "in position:", i)
            break;
        i = i + 1

    if found == False:
        print('item not found')

# ===== Main body =====
lst = [52, 15, 62, 84, 68, 44]
src = int(input('enter a number:'))

# forloop(lst,src)
whileloop(lst,src)