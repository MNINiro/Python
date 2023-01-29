ItemNumber = []
Description = []
ReservePrice = []
NoOfBids = []
Sold = []

noBid = 0
sold = 0

for count in range(2):
    ItemNo = int(input("Enter Item Number:"))
    ItemNumber.append(ItemNo)

    Desc = input("Enter Description:")
    Description.append(Desc)

    ResPrs = int(input("Enter Reserve Price:"))
    ReservePrice.append(ResPrs)

    noBid += 1
    NoOfBids.append(noBid)

    Sold.append(sold)
    print()

# print("Item Number:", ItemNumber)
# print("Description:", Description)
# print("Reserve Price:", ReservePrice)
# print("No of Bids:", NoOfBids)
# print("Sold Status:", Sold)


print(ItemNumber[0], " ", Description[0]," ", ReservePrice[0], " ", NoOfBids[0]," ",Sold[0])
print(ItemNumber[1], " ", Description[1]," ", ReservePrice[1], " ", NoOfBids[1]," ",Sold[1])