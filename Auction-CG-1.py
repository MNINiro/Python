# Auction Program

# Item class to store information about each item
class Item:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.number_of_bids = 0
        self.highest_bid = 0


# Auction class to store information about the auction and items
class Auction:
    def __init__(self):
        self.items = []

    # Method to add an item to the auction
    def add_item(self, item_number, description, reserve_price):
        new_item = Item(item_number, description, reserve_price)
        self.items.append(new_item)

    # Method to find an item by item number
    def find_item(self, item_number):
        for item in self.items:
            if item.item_number == item_number:
                return item
        return None

    # Method to place a bid on an item
    def place_bid(self, buyer_number, item_number, bid):
        item = self.find_item(item_number)
        if item is not None and bid > item.highest_bid:
            item.highest_bid = bid
            item.number_of_bids += 1
            print("Bid placed successfully. Item Number: {}, Description: {}, Current highest bid: {}".format(
                item.item_number, item.description, item.highest_bid))
        else:
            print("Invalid bid. Please enter a bid higher than the current highest bid.")

    # Method to end the auction and calculate fees
    def end_auction(self):
        for item in self.items:
            if item.highest_bid > item.reserve_price:
                item.sold = True
                fee = item.highest_bid * 0.1
                print("Item Number: {}, Description: {}, Reserve Price: {}, Final bid: {}, Fee: {}".format(
                    item.item_number, item.description, item.reserve_price, item.highest_bid, fee))
            else:
                item.sold = False
                print("Item Number: {} not sold".format(item.item_number))


# Initialize auction
auction = Auction()

# Add items to the auction
auction.add_item(1, "Antique vase", 500)
auction.add_item(2, "Painting by Monet", 2000)
auction.add_item(3, "Sculpture by Rodin", 1500)

# Find an item and view information
item = auction.find_item(2)
print("Item Number: {}, Description: {}, Reserve Price: {}".format(item.item_number, item.description,
                                                                   item.reserve_price))

# Place a bid on an item
auction.place_bid(1, 2, 2100)
auction.place_bid(2, 2, 2000)
auction.place_bid(3, 2, 2200)

# End the auction and calculate fees
auction.end_auction()
