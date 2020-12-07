#=== Ex-1 ===
my_list = ["el1", "el2", "el3", "el4"]
pos = my_list.index("el3")
print(f"{pos} Position in the list")

#=== Ex-2 === Duplicate elements
my_list1 = ["el3", "el2", "el3", "el4"]
pos = my_list1.index("el3") #it will only show the first element of the list
print(f"{pos} Position in list")


#=== Ex-3 === Duplicate elements
my_list1 = [1,2,3,1,4,1,5,1,5]
lst = [i for i in range(len(my_list1)) if my_list1[i]==1]
print(f"{lst} Position in list")

