#=== Ex-1 ===
lst = [1,4,2,3,1,2,1,4]
n = lst.count(1)
print(n,"times integer")

#=== Ex-2 ===
lst = ['a','s','d','a','c','d']
n = lst.count('a')
print(n,"times character")

#=== Ex-3 ===
lst = [1,4,2,3,1,2,1,4,'a','s','d','a','c','d']
n = lst.count(4)
m = lst.count('d')
print(f"{n},'times integer' and {m},'times character'")
