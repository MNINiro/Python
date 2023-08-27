SetA = {3, 5, 10, 12, 5, 20}
SetB = {3, 5, 10}

# print(len(SetB))
# print('Union:', SetA.union(SetB))

print('Difference:', SetA.difference(SetB))
print('Difference:', SetB.difference(SetA))
print('Intersection:', SetA.intersection(SetB))
# print(SetA.pop())
# print(SetB.pop())

print(SetA.issubset(SetB))
print(SetB.issubset(SetA))

# print(SetA.clear())
# print(SetA)

SetA.remove(10)
# print(SetA)

SetA.add(100)
print(SetA)


# print(len(SetB))
# for i in SetA:
#     print(i)





















# ====================================

# x = "A Python Tutorial"
# print('Tuple: ',tuple(x))
# print('List: ',list(x))
# print('Set: ',set(x))
# ====================================
# cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
# NewCities = set(['Paris', 'Birmingham', 'Lyon', 'London', 'Berlin'])
# print(cities)
# print(NewCities)
# =================================

# Adding new value in a set
# colours = {"red","green"}
# print(colours)
#
# colours.add("brown")
# colours.add("yellow")
# print(colours)

# you can't add more than one element in a set at a time
# colours.add("black","white")

# for i in range(3):
#     x = input("Enter new colour: ")
#     colours.add(x)
# print(colours)
#
# #to romove an item from the set
# colours.remove("red")
# colours.remove("brown")
# print(colours)
#
# #to remove everything from a set
# colours.clear()
# print(colours)
