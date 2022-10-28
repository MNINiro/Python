import pprint as p, pickle

file = open('D:/data.pkl', 'rb')

data1 = pickle.load(file)
p.pprint(data1)

data2 = pickle.load(file)
p.pprint(data2)

file.close()
