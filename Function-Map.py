# to apply specific rule on each data of the list
a = [10,20,30,40,50]
# b = [1,2,3,4,5]

# # ===Ex-1===
def inc(n):
    return n * 2

result = map(inc,a)
print(result) #it will show memory location
print(type(result))
for i in result:
    print(i)

# #=== Ex-2 ===
result = list(map(lambda n: n+2, a))
print(result)
print(type(result))
for i in result:
    print(i)

# # #=== Ex-3 ===
# result = list(map(lambda n,m: n+m, a,b)) #a and b will pass values to n and m respectively
# print(result)
# print(type(result))
# for i in result:
#     print(i)
#
# # #===Ex-4===
# def starts_with_A(s):
#     return s[0] == "A"
#
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(starts_with_A, fruit)
# print(list(map_object))
#
# #===Ex-5===
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(lambda s: s[0] == "A", fruit)
#
# print(list(map_object))