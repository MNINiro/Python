cities = {"Stuttgart", "Konstanz", "Freiburg"}
more_cities = {"Winterthur","Schaffhausen","St. Gallen"}

cities_backup = more_cities.copy()

print(cities)
print (more_cities)
print(cities_backup)

# # cities_backup = cities.copy()
# # print(cities_backup)
#
# #it will remove cities from more_cities but not from cities_backup
# more_cities.clear()
# print (more_cities)
# print(cities_backup)

#======== difference() =======================
#
# x = {"a","b","c","d","e"}
# y = {"b","c","u"}
# z = {"c","d","p"}

# print(x.difference(y))
# # # will show only uncommon values {'a', 'd', 'e'}
# #
# print(x.difference(y).difference(z))
# # will display only uncommon values {'e', 'a'}
# #
# # or we can write as follow:
# x = x - y - z
# print(x)

#======== discard=======================

# An element will be removed from the set,
# if it is contained in the set. If element is not a member of the set,
# nothing will be done.

# x = {"a","b","c","d","e"}
# x.discard("a")
# print(x)

# x.discard("z")
# print(x)



#======== remove(el)=======================

#works like discard(), but if el is not a member of the set,
# a KeyError will be raised.  

# x = {"a","b","c","d","e"}
# x.remove("a")
# print(x)

# x.remove("z")
# print(x)
