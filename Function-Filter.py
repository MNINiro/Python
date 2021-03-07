#to find values higher than the given value
a = [100,50,60,80,90,5,45,65]
# ===Ex-1===
def highMarks(n):
    if n >= 60:
        return True

result = filter(highMarks,a)
for i in result:
    print(i)
print(type(result))
print()

#===Ex-2===
# result = list(filter(highMarks,a))
# print(result)
# print(type(result))
# for i in result:
#     print(i)

#===Ex-3=== Alternate method using lambda ===
a = [100,50,60,80,90,5,45,65]
result = filter(lambda n: (n >= 60), a)
for i in result:
    print(i)
print(type(result))
print()

# #===Ex-4===
# a = [True,False,True,False,True]
#
# result = list(filter(None, a)) #only True will be displayed
# for i in result:
#     print(i)
# print(type(result))
# print()

