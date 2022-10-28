#========== intersection(s)===========

# Returns the intersection of the instance set and the set s as a new set.
# In other words:
# A set with all the elements which are contained in both sets is returned.

x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}

# use x.intersection(y) to get the result
# This can be abbreviated with the ampersand operator "&" like x  & y

print(x.intersection(y))

#========== isdisjoint(s)===========

#This method returns True if two sets have a null intersection.

x = {"a","b","c","d","e"}
y = {"h","i","j","f","g"}

#use x.isdisjoint(y) to get the result
print(x.isdisjoint(y))

#========== issubset()===========

# x.issubset(y) returns True, if x is a subset of y. "<=" is an abbreviation for
# "Subset of" and ">=" for "superset of" 
# "<" is used to check if a set is a proper subset of a set

x = {"a","b","c","d","e"}
y = {"c","d"}

# x.issubset(y) #to get the result "FALSE" and
# y.issubset(x) will return TRUE

print(x.issubset(y))
print(y.issubset(x))

# #========== issuperset()===========
# #x.issuperset(y) returns True, if x is a superset of y. ">=" is an abbreviation
# # for "issuperset of" ">" is used to check if a set is a proper superset of a set.

x = {"a","b","c","d","e"}
y = {"c","d"}
z = {"a","b","c","d","e"}

# x.issuperset(y)  will return TRUE
# y.issuperset(x)  will return FALSE
# print(x.issuperset(y))
# print(z.issuperset(x))
# print()
# print(x.issuperset(z))
# # print(z.issubset(y))
# print(x.issubset(z))
# print(z.issubset(x))

# #========== pop()===========
#
# # pop() removes and returns an arbitrary set element.
# # The method raises a KeyError if the set is empty

x = {"a","b","c","d","e"}

# x.pop() will remove an element randomely

print(x.pop())
print(x)























