lst = [23, 56, 1012, 67, 2, 89, 345]

mx = 0

for i in range(len(lst)):
    if lst[i] > mx:
        mx = lst[i]

print("Maximum value:", mx)


mn = 100000

for i in range(len(lst)):
    if lst[i] < mn:
        mn = lst[i]

print("Minimum value:", mn)