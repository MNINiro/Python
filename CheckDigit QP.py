def checkdigit(lst):
    j = 6       #5 digit car parking number
    total = 0

    for i in range(len(lst)-1):     # -1 for 4 times because 5th value is the check digit
        j -= 1                      # j = j-1
        total += int(lst[i]) * j    # lst[i] value of the ith position. converting string values into integer for calculation

    remainder = total % 11
    cd = 11 - remainder
    print("Check Digit is :", cd)
    print()

    if (cd == int(lst[4])):         #comparing check digit with the 5th value(also a check digit)
        print("Valid check digit")
        print('Do Discount code here')
    else:
        print('Invalid Parking number')

fcpn = str(input('Enter car parking no:'))
lst = list(fcpn)                #converting into a list. by default it is in string
print(lst)
checkdigit(lst)