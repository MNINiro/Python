value = int(input('Enter value:'))

while value != -1:
    if value >= 50 and value <= 100:
        Diff1 = 100 - value
        Diff2 = value - 50
        print(Diff1)
        print(Diff2)
        print()
        if Diff1 < 1 or Diff2 < 1:
            print("Accept:Extreme")
        else:
            print("Accept: Normal")
    else:
        print("Reject: Abnormal")

    value = int(input('Enter value:'))


