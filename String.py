def frequency(string = ''):
    store = dict()
    total = 0
    
    for char in string:
        total = store.items()
        store[char] = total
        
    return store

print(frequency(string='Hello world'))

#======================================


##store = {}
##string = "Hello World"
##
##for char in list(string):
##  if char not in store:
##    store[char] = 0
##  store[char] += 1
##
##for key, value in store.items():
##    print(key, value)


