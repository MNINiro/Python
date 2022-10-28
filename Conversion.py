Lst = [10, 20, 30,'A']
print('List:', Lst)

Tup = (101, 102, 'A', 'B')
print('Tuple:',Tup)

s = {122, 456, 233}
print('Set:', s)

print(Lst[0])
print(Lst[1])
print(Lst[2])
print()

print(Tup[0])
print(Tup[1])
print(Tup[2])
print(Tup[3])
print()

# print(s.pop())
st = set(Lst)
print('Converted to Set:', st)

t = tuple(Lst)
print('Converted to tuple:', t)

print(st.pop())