a = [5,5,6,7,7,7]
b = set(a)  #{5,5,6,7,7,7}
	
def test(lst):      #lst = a = [5,5,6,7,7,7]
    if lst in b:
        return 1
    else:
        return 0

for i in filter(test, a):
    print(i, end = " ")
