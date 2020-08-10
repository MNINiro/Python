# a = {3, 5, 10, 12, 20}
# for i in a:
# 	print (i)


#==================================== 

# x = "A Python Tutorial"
#
# # set(['A', ' ', 'i', 'h', 'l', 'o', 'n', 'P', 'r', 'u', 't', 'a', 'y', 'T'])
# # type(x)
# print(set(x))

#====================================
#
# cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
# NewCities = set(['Paris', 'Birmingham', 'Lyon', 'London', 'Berlin'])
# print(cities)
# print(NewCities)

###=================================

##x = set(["Perl", "Python", "Java"])
##
##set(['Python', 'Java', 'Perl'])

###=================================

colours = {"red","green"}
print(colours)

colours.add("brown")
colours.add("yellow")
print(colours)

# you can't add more than one element in a set at a time
##colours.add("black","white")

# #to remove everything from a set
colours.clear()
print(colours)
