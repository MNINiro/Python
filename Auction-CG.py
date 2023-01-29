# Constants
MIN_ITEMS = 3

# Variables
items = []


# Function to set up an auction
def set_up_auction():
    num_items = int(input("Enter the number of items in the auction: "))
    while num_items < MIN_ITEMS:
        print("Error: There must be at least", MIN_ITEMS, "items in the auction.")
        num_items = int(input("Enter the number of items in the auction: "))

    for i in range(num_items):
        item_num = int(input("Enter the item number: "))
        description = input("Enter the item description: ")
        reserve_price = float(input("Enter the reserve price: "))

        item = {
            "item_num": item_num,
            "description": description,
            "reserve_price": reserve_price,
            "num_bids": 0,
            "highest_bid": 0
        }
        items.append(item)


# Function to place a bid
def place_bid(buyer_num):
    item_num = int(input("Enter the item number: "))
    item = None
    for i in items:
        if i["item_num"] == item_num:
            item = i
            break
    if item == None:
        print("Error: Item not found.")
        return
    print("Item:", item["item_num"])
    print("Description:", item["description"])
    print("Current highest bid:", item["highest_bid"])

    bid = float(input("Enter your bid: "))
    while bid <= item["highest_bid"]:
        print("Error: Bid must be higher than the current highest bid.")
        bid = float(input("Enter your bid: "))
    item["highest_bid"] = bid
    item["num_bids"] += 1
    print("Bid placed.")


# Variables
total_fee = 0
items_sold = 0
items_not_met_reserve = 0
items_no_bids = 0


# Function to end the auction
def end_auction():
    global total_fee, items_sold, items_not_met_reserve, items_no_bids
    for item in items:
        if item["num_bids"] == 0:
            items_no_bids += 1
            print("Item", item["item_num"], "received no bids.")
        elif item["highest_bid"] >= item["reserve_price"]:
            items_sold += 1
            fee = item["highest_bid"] * 0.1
            total_fee += fee
            print("Item", item["item_num"], "sold for", item["highest_bid"], "with a fee of", fee)
        else:
            items_not_met_reserve += 1
            print("Item", item["item_num"], "did not meet the reserve price")


# Test the function
set_up_auction()
print("Auction set up complete.")

# Test the function
buyer_id = int(input("Enter Buyer Id:"))
place_bid(buyer_id)

end_auction()
