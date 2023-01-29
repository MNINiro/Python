Total = 0
Count = 0
weight = int(input("Enter the weight of the basket:"))

while weight != -1:
    Total += weight
    Count += 1
    print(Total, 'and', Count)
    weight = int(input("Enter another weight:"))

print("The total weight is:", Total)
print("The number of baskets are:", Count)