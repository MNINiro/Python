import json

list = [1, 2, (3, 4)] # Note that the 3rd element is a tuple (3, 4)
print(json.dumps(list)) # '[1, 2, [3, 4]]'


import json
j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
print (j['two'])
