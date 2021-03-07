# quantity = int(input("Input the quantity of an item: "))
# discount = 0
# order_price = 0
#
# if quantity >= 10:
#     discount = 5
# if quantity >= 20:
#     discount = 10
# if quantity >= 50:
#     discount = 25
# if quantity >= 100:
#     discount = 35
# if quantity >= 500:
#     discount = 50
#
# error = 1
# while error == 1:
#     if price[buy_position] * stock_amount[buy_position] > 50:
#         voucher = str(input("Use the $10 coupon? (y/n): "))
#         if voucher == 'y' or voucher == 'Y':
#             price[buy_position] * stock_amount[buy_position] = price[buy_position] * stock_amount[buy_position] - 10
#             error = 0
#         elif voucher == 'n' or voucher == 'N':
#             price[buy_position] * stock_amount[buy_position] = price[buy_position] * stock_amount[buy_position]
#             error = 0
#         else:
#             print("Not a valid answer.")
#             error = 1

item_name = ['pen','ruler', 'copy']
item_code = ['1A01','1A04','1B01']
description = ['black pen','5cm scale','blnk copy']
price = [10,20,40]
stock_amount = [50,20,35]

print('Item code, Description, Price, Stock amount')

ln = len(item_name)
i = 0
while (i < ln):
    print(f"{item_code[i]}      {description[i]}     {price[i]}        {stock_amount[i]}")
    i += 1

error = 1
while error == 1:
    buy_item_code = str(input("Enter the item code of the item you want to buy: "))
    if buy_item_code == 'stop':
        error = 0
    elif (buy_item_code not in item_code) == True:
        print("Item code not available.")
    elif (buy_item_code not in item_code) == False:
        buy_position = item_code.index(buy_item_code)
        print(f"The item you're buying is {item_name[buy_position]}.")
        if stock_amount[buy_position] <= 0:
            print("Item not in stock.")
        elif stock_amount[buy_position] <= 10:
            print("Item low on stock.")
            quantity = int(input("Enter the quantity of item you want to buy: "))
            if quantity > stock_amount[buy_position]:
                print("Your order is rejected.")
            else:
                confirm = str(input("Confirm order? (y/n/stop): "))
                error2 = 1
                while error2 == 1:
                    if confirm == 'y' or confirm == 'Y':
                        print("Order confirmed successfully.")
                        stock_amount[buy_position] = stock_amount[buy_position] - quantity
                        error2 = 0
                    elif confirm == 'n' or confirm == 'N':
                        print("Your order was cancelled.")
                        error2 = 0
                    elif confirm == 'stop':
                        error = 0
                        error2 = 0
                    else:
                        print("Not a valid input.")
        else:
            quantity = int(input("Enter the quantity of item you want to buy: "))
            if quantity > stock_amount[buy_position]:
                print("Your order is rejected.")
            else:
                confirm = str(input("Confirm order? (y/n/stop): "))
                error2 = 1
                while error2 == 1:
                    if confirm == 'y' or confirm == 'Y':
                        print("Order confirmed successfully.")
                        stock_amount[buy_position] = stock_amount[buy_position] - quantity
                        error2 = 0
                    elif confirm == 'n' or confirm == 'N':
                        print("Your order was cancelled.")
                        error2 = 0
                    elif confirm == 'stop':
                        error = 0
                        error2 = 0
                    else:
                        print("Not a valid input.")
i = 0
while i < ln:
    if stock_amount[i] == 0:
        print(f"The item {item_name[i]} is out of stock.")
    i+=1

