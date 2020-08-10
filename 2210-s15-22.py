Name = []
Weight = []

for i in range(2):

    n = input("Enter Name :")
    Name.append(n)

    w = float(input("Enter Weight :"))

    while True:
        if (w >= 30) and (w <= 100):
            Weight.append(w)
            break
        else:
            print("Invalid weight entered")
            w = int(input("Enter Weight :"))


for i in range(2):
    print("The Student's Name is",Name[i], "and Weight is",Weight[i])

NWeight = []
WDifference = []

for i in range(2):
    nw = float(input('Enter Last Day Weight: '))
    NWeight.append(nw)
    d = NWeight[i] - Weight[i]
    WDifference.append(d)

    if d > 2.5:
        print('Weight rise on Last Day Is:', WDifference[i])
    elif d < 2.5:
        print('Weight lost on Last Day Is:', WDifference[i])


# for i in range(2):
#     print('Weight Differences on Last Day Is:', WDifference[i])

