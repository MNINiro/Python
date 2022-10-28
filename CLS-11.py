NAME = []
TOTAL = []

# print('Before appending Names:', NAME)

for name in range(3):
    nm = input('Enter Student name:')
    NAME.append(nm)

    tot = 0
    for marks in range(3):
        mrk = float(input('Enter marks:'))

        if mrk < 0 or mrk > 100:
            print('Invalid marks entered')
        else:
            tot = tot + mrk
    TOTAL.append(tot)

print("======Output=========")

for count in range(3):
    print(NAME[count], ':', TOTAL[count])
