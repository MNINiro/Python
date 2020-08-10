f = ['a', 'b', 'd']
f.insert(2, 'c')  # Insert item "c" before index 2

print(f)


#trickier, method is to replace a single element
#slice of the list with a multi-item list like 

f = ['a', 'b', 'd']
f[1:2] = [f[1], 'c']

##Here we’re replacing from item 1 (the second item due to zero-indexing)
##up to (but not including) index 2 (a single element slice) with the item
##at index one (thus keeping it, unchanged) and the new item. 

print(f)
