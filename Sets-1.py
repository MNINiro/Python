# mySet = {3, 5, 10, 12, 20}
# for i in mySet:
#     print(i)
# print(mySet)


#==================================== 
# x = "A Python Tutorial"
#
# # set(['A', ' ', 'i', 'h', 'l', 'o', 'n', 'P', 'r', 'u', 't', 'a', 'y', 'T'])
# # type(x)
# print('List: ',list(x))
# print('Set: ',set(x))
# print('Tuple: ',tuple(x))

#====================================
# cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
# NewCities = set(['Paris', 'Birmingham', 'Lyon', 'London', 'Berlin'])
# print(cities)
# print(NewCities)

###=================================
colours = {"red","green"}
print(colours)

colours.add("brown")
colours.add("yellow")
print(colours)

# # you can't add more than one element in a set at a time
# colours.add("black","white")

# for i in range(3):
#     x = input("Enter new colour: ")
#     colours.add(x)
# print(colours)

#to romove an item from the set
colours.remove("red")
colours.remove("brown")
print(colours)

# # #to remove everything from a set
colours.clear()
print(colours)
