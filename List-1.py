## DECLARE M AS LIST
## DECLARE N AS INTEGER

l = ['a','b','c','d']
m = ['muhit','tasdeeq']

print(l[2])
print(len(l))
print(m[0][2])

def namelist():
    m = ['Muhit','Labib','Nabiha']
    n = ['Tasdeeq','Momtahina','Esha']
    x = []
    print(x)

    for i in range(3):
        x.append('Rafi')
        x.append('Akif')

        x.append(m[i])
        x.append(n[i])
        print(x)

namelist()
