import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

file = open('D:/data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, file)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, file, -1)

file.close()
