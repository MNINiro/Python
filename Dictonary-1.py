d = {'cat': 'cute',
     'dog': 'furry'}  # Create a new dictionary with some data

print(d['cat'])       # Get an entry from a dictionary; prints "cute"
print(d['dog'])
print()

print('cat' in d)     # Check if a dictionary has a given key; prints "True"
print('fish' in d)
print()

#adding a new item in the dictionary
d['fish'] = 'wet'     # Set an entry in a dictionary
print(d['fish'])      # Prints "wet"
print('fish' in d)
print(d)
print()

# print(d['monkey'])  # KeyError: 'monkey' not a key of d
#
# temporary addition to avoid KeyError
print(d.get('monkey', 'Jumps'))  # Get an element with a default; prints "Jumps"
print(d.get('bird', 'Fly'))    # Get an element with a default; prints "Fly"
print(d)
# #
del d['fish']         # Remove an element from a dictionary
print(d)
#
print(d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"
#
#
