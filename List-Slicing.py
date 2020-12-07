#=== Ex-1 ===
lst = [1,4,2,3,1,2,1,4]
print("Before slicing",lst)

nl = lst[0:3]
print("After Slicing",nl)

nl = lst[3:6]
print("After Slicing",nl)

nl = lst[0:3:1]
print("After Slicing with 1 step",nl)

nl = lst[0:6:2]
print("After Slicing with 2 step",nl)

nl = lst[0:7:3]
print("After Slicing with 3 step",nl)

nl = lst[:-3]
print("After Slicing with -3 step",nl)

nl = lst[-7:-3]
print("After Slicing with -7 to -3 step",nl)

for i in nl:
    print(i)