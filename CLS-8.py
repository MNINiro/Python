def add(data1, data2):
    result = data1 + data2
    print('Addition:', result)
    return result


def sub(data1, data2):
    result = data1 - data2
    print('Subtraction:', result)

    x = add(result, data2)
    result = x - result
    print('updated result:', result)
    return result


# ========= Main Body ===========
# add(25, 15)     #parameter passing or passing arguments through parameter

d1 = int(input('Enter 1st data:'))
d2 = int(input('Enter 2nd data:'))

sub(d1, d2)





def mult(data1, data2):
    result = data1 * data2
    print('Multiplication:', result)
    return result


def div(data1, data2):
    result = data1 / data2
    print('Division:', result)
    return result
# x = add(d1, d2)
# print('outside function:', x)
# y = sub(d1, d2)
# z = mult(d1, d2)
# k = div(d1, d2)
