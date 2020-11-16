print("༶•-----⛧♛Sellers' page♛⛧-----•༶")
print()

item_number_list = []
detail_list = []
highest_bid_list = []
highest_bid = 0

number_of_items = int(input("Enter the number of items: "))

for i in range(number_of_items):
    insert_item_number = str(input(f"Insert item number: "))


    if insert_item_number != insert_item_number:
        print("Item number already exists!")

    item_detail = str(input("Enter item details: "))
    reserve_price = input("Enter your reserve price: ")
    item_number_list.append(insert_item_number)
    detail_list.append(item_detail)
    highest_bid_list.append(reserve_price)

print(f"Item numbers list: {item_number_list}")
print()

#===================================================================================================#

print("⋇.*✦⋆✦⋇Buyers' page⋇✦⋆✦*.⋇")
print()
print(f"Item numbers list: {item_number_list}")
print()
buyer_id = str(input("Enter buyer id: "))

search_number = 0


while search_number != 'skip':
    search_item_number = str(input("Enter item number (or type 'skip' to skip): "))
    search_number = search_item_number

    if (search_item_number not in item_number_list) == True:
        print("This item number doesn't exist...")
    else:
        print(f"Item number: {search_item_number}")
        print(f"Item details: {detail_list[item_number_list.index(search_item_number)]}")
        print(f"Reserve price/ Current highest bid: {highest_bid_list[item_number_list.index(search_item_number)]}")

print()

bid_count = 0
bid_amount = 0
bid_item = 0
int_highest_bid = int(reserve_price)

while bid_item != 'skip':
    bid_item = input("Enter the item number you want to bid for (type 'skip' to skip): ")
    if (bid_item not in item_number_list) == True:
        print("This item number doesn't exist...")
    else:
        bid_amount = int(input("Enter the amount you want to bid: "))
        bid_count += 1

    if bid_amount < int(int_highest_bid):
        print("You cannot bid lower than the reserve price/previous bid value.")
    else:
        bid_amount = highest_bid
        print("You have successfully bid your amount.")

print(f"Number of bids made: {bid_count}")


print(f"The auction fee: {int_highest_bid}")
print(f"The auction company fee: {int_highest_bid*10/100}")
print(f"Total fee: {int_highest_bid*10/100+int_highest_bid}")





