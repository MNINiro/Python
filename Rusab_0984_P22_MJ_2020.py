days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
while True:
    dayInput = str(input('Enter the day of entry: ')).upper()
    hourInput = int(input("Enter hours for stay: "))
    hourOfArrival = int(input('Enter hour of arrival (24hr format, example: 14): '))
    if dayInput in days:
        fpn = int(input("Enter your frequent parking number: "))
        s = 0
        position = 5
        while (fpn > 0):
            digit = fpn % 10
            s = (digit * position) + s
            position = position - 1
            fpn = int(fpn / 10)

        mod = s % 11
        cd = 11 - mod
    ##    print(cd, is the check digit)

        if hourOfArrival>=8 and hourOfArrival<= 15:
            if cd==4:
                discount = 0.9
            else:
                discount = 1
            if dayInput == "SUNDAY" and hourInput<= 8:
                pph = 2.00
            elif dayInput == "MONDAY" and hourInput<=2:
                pph = 10.00
            elif dayInput == "TUESDAY" and hourInput<=2:
                pph = 10.00
            elif dayInput == "WEDNESDAY" and hourInput<=2:
                pph = 10.00
            elif dayInput == "THURSDAY" and hourInput<=2:
                pph = 10.00
            elif dayInput == "FRIDAY" and hourInput<=2:
                pph = 10.00
            elif dayInput == "SATURDAY" and hourInput<=4:
                pph = 3.00
            else:
                print("Hours entered outside range. Please re-check the sheet for appropriate timings.")
                continue
    else:
        print("Please re-enter the day: ")
        continue
    print('Your discount is', discount)
    print("Total price is", (pph * hourInput) * discount )






