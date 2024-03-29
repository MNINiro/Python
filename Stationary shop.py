item_code=["1A17", "1B18", "1C19", "1D20", "1E21"]
item_name=['pen', 'pencil', "eraser", "sharpener", "paper"]
item_price=[10,15,6,12,7]
item_stock=[70,0,25,61,19]

def inventory():
    print(f'item code, name, price, stock')
    for i in range(len(item_code) - 1):
        print(f"{item_code[i]}, {item_name[i]}, {item_price[i]}, {item_stock[i]}")
    print('--------------------------------------------')


def buyer():
    searchCode = str(input('please enter the item code of the product: '))
    if (searchCode not in item_code) == True:
        print("item not in inventory. please try again")
        print('---------------------------------------')
        print(shopper())
    elif (searchCode in item_code) == True:
        searchPos = item_code.index(searchCode)
        if (item_stock[searchPos] <= 0) == True:
            print('item out of stock')
            print('---------------------------------------')
            print(inventory())
            buy_amount = int(input("enter the amount to buy: "))
            if (buy_amount <= item_stock[searchPos]) == True:
                print(discount())
                print("total amount is", buy_amount * item_price[searchPos])
                print('confirm order?')
                confirmation = input("(yes/no):")
                if confirmation == 'yes':
                    item_stock[searchPos] = item_stock[searchPos] - buy_amount
                    print('order confirmed')
                    print('---------------------------------------')
                    print('new inventory: ')
                    print(inventory())
                    print(shopper())
                elif confirmation == 'no':
                    print('order cancelled')
                    print('---------------------------------------')
                    print(shopper())
            elif (buy_amount > item_stock[searchPos]) == True:
                print('stock not enough to fulfill order.')
                print('---------------------------------------')
                print(shopper())
    elif item_stock[searchPos] <= 10:
            print('item low on stock')
            buy_amount = int(input("enter the amount to buy: "))
            if (buy_amount <= item_stock[searchPos]) == True:
                print(discount())
                print("total amount is", buy_amount * item_price[searchPos])
                print('confirm order?')
                confirmation = input("(yes/no):")
                if confirmation == 'yes':
                    item_stock[searchPos] = item_stock[searchPos] - buy_amount
                    print('order confirmed')
                    print('---------------------------------------')
                    print('new inventory: ')
                    print(inventory())
                    print(shopper())
                elif confirmation == 'no':
                    print('order cancelled')
                    print('---------------------------------------')
                    print(shopper())
            elif (buy_amount > item_stock[searchPos]) == True:
                print('stock not enough to fulfill order.')
                print('---------------------------------------')
                print(shopper())

    elif item_stock[searchPos] > 10:
            print(subbuyer())


def shopper():
    print('would you like to shop today?')
    variable = input('(y/n):')
    if (variable == "y") == True:
        print(buyer())
    elif (variable == 'n') == True:
        print("have a nice day!")
    else:
        print('invalid response. plz try again')
        print(shopper())

def discount():
    dscnt = 0
    if buy_amount >= 500:
        dscnt = 50/100
    elif buy_amount >= 100:
        dscnt = 35/100
    elif buy_amount >= 50:
        dscnt = 25/100
    elif buy_amount >= 20:
        dscnt = 10/100
    elif buy_amount >= 10:
        dscnt = 5/100
    print(f'discount is {dscnt}')



print(inventory())
print(shopper())




