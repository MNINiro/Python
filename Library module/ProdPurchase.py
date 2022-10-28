def purchase():
    name = []
    qty = []
    price = []
    purchase_total = 0
    cont = 'Y'

    while cont != 'N':
        proName = input('Enter Product Name: ')
        name.append(proName)

        proQty = int(input('Enter Quantity: '))
        qty.append(proQty)

        proPrice = float(input('Enter Price: '))
        price.append(proPrice)

        purchase_total += proPrice * proQty
        print(purchase_total)

        cont = input('Do you want to continue (y/n):')
        cont = cont.upper()

    print("Items\t Quantity\t price\t sub-total")
    ln = len(name)

    for i in range(ln):
        print(name[i], '      ', qty[i], '        ', price[i], '        ', qty[i] * price[i])

    print('-' * 50)
    print('Total purchase price:', purchase_total)

    return purchase_total