import operator

l = [9, 4, 0.03]

m = [[0, 1, 0.213], [4, 2, 0.12], [9, 4, 0.03]]

sorted_list = sorted(l)
print(sorted_list)

#Ascending order

sorted_list = sorted((sorted(m), key=operator.itemgetter(1)))
print(sorted_list)

#Descending Order

sorted_list = sorted(m, key=operator.itemgetter(2))
print(sorted_list)
