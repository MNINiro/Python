# the item numbers, buyer numbers and item descriptions are predefined

itemNumber = [ 534, 296, 339, 112, 354, 399, 612, 786, 451, 487]
reservedPrice = [ 10, 15, 25, 17, 30, 12, 22, 34, 28, 40]
description = [ 'a', 'b', 'c', 'd', 'e' ]
buyerNumber = [ 1054, 1063, 1042 ]
numberOfBids = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
highestBid = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totalPrice = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


inputNewBid = 0
inputBuyerNumber = 0
inputItemNumber = 0
itemValidity = False
buyerValidity = False
auctionStatus = True
itemsSold = 0
itemsUnderRP = 0
itemsNoBids = 0

while auctionStatus == True:
    inputItemNumber = input("\n\nEnter an Item Number to search: ")

    while itemValidity == False:
        for i in itemNumber:
            if int(inputItemNumber) == i:
                itemValidity = True

        if itemValidity == False:
            inputItemNumber = input("Invalid Item Number. Try again: ")


    index = itemNumber.index(int(inputItemNumber))

    print("\n\tItem Number: ", inputItemNumber, 
          "\n\tDescription: ", description[index],
          "\n\tHighest Bid: ", highestBid[index])


    inputBuyerNumber = input("\nEnter Buyer Number to bid: ")

    while buyerValidity == False:
        for i in buyerNumber:
            if int(inputBuyerNumber) == i:
                buyerValidity = True
        if buyerValidity == False:
            inputBuyerNumber = input("Invalid Buyer Number. Try again: ")

    inputNewBid = input("\nEnter your bid: ")

    while int(inputNewBid) <= highestBid[index]:
        inputNewBid = input("Your bid must be higher than the current highest bid. Try again: ")

    highestBid[index] = int(inputNewBid)
    numberOfBids[index] = numberOfBids[index] + 1

    decision = input("\nPress Enter to bid again. (Enter 'e' to end the auction): ")
    if decision == "e":
        auctionStatus = False


count = 0
while count < len(itemNumber):
    if highestBid[count] >= reservedPrice[count]:
        totalPrice[count] = round((highestBid[count] / 100) * 110)
        itemsSold = itemsSold + 1
        print("\n\tItem Number: ", itemNumber[count], "\t|\tSold\t|\t", "Total Price: ", totalPrice[count])
    elif highestBid[count] > 0:
        totalPrice[count] = highestBid[count]
        itemsUnderRP = itemsUnderRP + 1
        print("\n\tItem Number: ", itemNumber[count], "\t|\tFinal Bid: ", totalPrice[count])
    else:
        itemsNoBids = itemsNoBids + 1
        print("\n\tItem Number: ", itemNumber[count])
    
       
    count = count + 1

print("\n\n\tItems sold: ", itemsSold, "\n\tItems not meeting reserved price: ", itemsUnderRP, "\n\tItems with no bids: ", itemsNoBids)
print("\n\n")
