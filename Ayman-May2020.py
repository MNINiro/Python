time = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
days_10 = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
days_2 = ['sunday']
days_3 = ['saturday']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def billprinter():
    print('enter (total) in day for daily total')
    print('enter (exit) in day to exit program')
    day = str(input('Enter day: '))
    total = 0
    if day in days:
        entry = int(input('Enter arrival hour: '))
        Exit = int(input('Enter exit hour: '))
        hours = Exit - entry
        if entry in time:
            if (day in days_10) and (hours <= 2):
                bill = hours * 10
                print('your bill is', bill)
                print('------------------------------------')
                print(billprinter())
            elif (day in days_3) and (hours <= 4):
                bill = hours * 3
                total = + bill
                print('your bill is', bill)
                print('------------------------------------')
                print(billprinter())
            elif (day in days_2) and (hours <= 8):
                bill = hours * 2
                total = + bill
                print('your bill is', bill)
                print('------------------------------------')
                print(billprinter())
            elif (entry <= 16) and (Exit >= 24):
                bill = 2
                total = + bill
                print('your bill is', bill)
                print('------------------------------------')
                print(billprinter())
            else:
                print('Not allowed, plz input info again')
                print(billprinter())
        else:
            print('Not allowed, plz input info again')
            print(billprinter())
    elif day == 'total':
        print("today's total:", total)
        print('would you like to go (back) or (exit)?')
        response = str(input('enter response: '))
        if response == 'back':
            print(billprinter())
        else:
            print('goodbye')
    elif day == 'exit':
        print('goodbye')
    else:
        print('Not allowed, plz input info again')
        print(billprinter())


print(billprinter())
