a = [5,5,6,7,7,7]
b = set(a)
	
def test(lst):
    if lst in b:
        return 1
    else:
        return 0

for i in filter(test, a):
    print(i, end = " ")
