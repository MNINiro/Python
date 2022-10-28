lst = [12, 546, 23, 89, 34, 90, 33]
# print(max(lst))
# print(tuple(reversed(lst)))
#
#
# # For tuple
# seqTuple = ('g', 'e', 'e', 'k', 's')
# print(list(reversed(seqTuple)))

for i in range(len(lst)):
    if lst[i] % 2 == 1:
        print(lst[i])

'''
def asterisk(s):
    print('*' * s)


lt = ["Hello", "World", "in", "a", "frame"]
s = 9
es = ' '
asterisk(s)
for i in lt:
    if len(i) == 5:
        print('*', i, '*')
    else:
        d = 5 - len(i)
        print('*', i, es * (d - 1), '*')

asterisk(s)
'''
