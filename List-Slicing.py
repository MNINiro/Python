#=== Ex-1 ===
lst = [1,2,3,4,5,6,7,8,9]
print("Before slicing",lst)

nl = lst[0:3]
print("After Slicing",nl)
#
# nl = lst[3:6]
# print("After Slicing",nl)
#
# nl = lst[0:3:1]
# print("After Slicing with 1 step",nl)
#
# nl = lst[1:8:2]
# print("After Slicing with 2 step",nl)
# #
# nl = lst[0:7:3]
# print("After Slicing with 3 step",nl)
#
# nl = lst[-3:]
# print("After Slicing with -3: ",nl)
#
nl = lst[-7:-3]
print("After Slicing with -7 to -3 step",nl)

for i in nl:
    print(i)