# x = int(input('Enter age:'))
#
# while x < 20:
#     print('child!!!')
#     x = int(input('Enter data:'))
#
# print('Adult')


# ===============
y = []
x = str(input('Enter flight 2s/4s/hp:'))
x = x.upper()

while (x != '2S') and (x != '4S') and (x != 'HP'):
    print('Wrong flight has been chosen!', x)
    x = str(input('Enter data:'))
    x = x.upper()
else:
    y.append(x)
    print(y)
