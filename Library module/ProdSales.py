def sales():
    name = []
    qty = []
    price = []
    sales_total = 0
    cont = 'Y'

    while cont != 'N':
        proName = input('Enter Product Name: ')
        name.append(proName)

        proQty = int(input('Enter Quantity: '))
        qty.append(proQty)

        proPrice = float(input('Enter Price: '))
        price.append(proPrice)

        sales_total += proPrice * proQty
        print(sales_total)

        cont = input('Do you want to continue (y/n):')
        cont = cont.upper()

    print("Items\t Quantity\t price\t sub-total")
    ln = len(name)

    for i in range(ln):
        print(name[i], '      ', qty[i], '        ', price[i], '        ', qty[i] * price[i])

    print('-' * 50)
    print('Total sales price:', sales_total)

    return sales_total