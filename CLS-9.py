# y = 1
# for x in range(5):
#     y = y + x
#     print(y)

def nestedLoop(start, end):
    for bw in range(start+2, end+2):
        for sw in range(1, 11):
            print(bw, 'X', sw, '=', bw * sw)
        print()

# nestedLoop(13,15)

# ======================================
# a = 0
# while (a < 5):
#     print(a**2)
#     a += 1

a = 1
while a < 3:
    b = 1
    while b < 3:
        print(a*b)
        b += 1
    a += 1
# ======================================
"""
def add(data1, data2):
    result = data1 + data2
    print('Inside add function:', result)
    return result


def sub(data1, data2):
    result = data1 - data2
    print('Inside sub function:', result)

    s1 = add(result, data2)
    print('From add:', s1)
    return result

# ======== Main Body ============
d1 = int(input('Enter first data:'))
d2 = int(input('Enter second data:'))

# x = add(d1, d2)
# print('Addition result:', x)
# print(x + 100)
# print()

y = sub(d1, d2)
print('Subtraction result:', y)
"""













