# import array as arr
# ThisArray = arr.array('str', ['Dhaka', 'Chittagong', 'Rajshahi', 'Barishal', 'Khulna'])

ThisArray = ['Dhaka', 'Chittagong', 'Rajshahi', 'Barishal', 'Khulna']


def ScanArray(SearchString):
    Index = 1
    Total = 0
    Error = False

    while (Index <= 1000) and (Error != True):
        if len(ThisArray[Index]) > 5:
            ThisElement = ThisArray[Index]
            if ThisElement[:4] == SearchString:
                Total = Total + len(ThisArray[Index]) - 5
            Index = Index + 1
        else:
            Error = True

    if Index > 1:
        ArrayResult = int(Total / (Index - 1))


print(ScanArray("Khulna"))
