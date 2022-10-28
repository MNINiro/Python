def dayCarPark(userCar, dailyCarsPayTotal):
    validity = False
    global carPark_payment
    global money_amt
    global now_hour
    money_amt = 0

    def dailyPayments(now_hour, dailyCarsPayTotal, money_amt):
        if now_hour == 24:
            print("The total amount of money earned today: ", dailyCarsPayTotal)
            dailyCarsPayTotal = 0

        else:
            valid = False
            while valid == False:
                user_moneyPay = float(input("How much will you pay?: "))
                if user_moneyPay < money_amt:
                    print("You cannot pay an amount less than amount displayed.")
                else:
                    valid = True

                    moneyChange = user_moneyPay - money_amt
                    print("You have a change of ", moneyChange, "but we're sorry, giving changes is not in our policy.")
                    dailyCarsPayTotal = dailyCarsPayTotal + user_moneyPay
                    print("The daily total so far: ", dailyCarsPayTotal)
                    dayCarPark(userCar, dailyCarsPayTotal)

    def freqParkNumDiscount(money_amt, now_hour):
        modulo_calc = ""
        result = 0
        j = 9
        user_option = str(input("Do you have a frequent parking number? "))
        if user_option.lower() == "no" or user_option.lower() == "n":
            print("Total amount: ", money_amt)
            dailyPayments(now_hour, dailyCarsPayTotal, money_amt)
        elif user_option.lower() == "yes" or user_option.lower() == "y":
            valid = False
            while valid == False:
                freqParkNum = str(input("Enter the frequent parking number: "))
                if len(str(freqParkNum)) != 5:
                    print("The code must be 5 digits long.")
                else:
                    valid = True
            lst = list(freqParkNum)
            for i in range(0,4):
                j -= 1
                result += int(lst[i]) * j

            remainder = result % 11
            cd = 11 - remainder

            if (cd == int(lst[4])):
                print("Your frequent parking number is valid.")
                if now_hour >= 16 and now_hour < 24:
                    print("You will get 50% discount from your car park payment.")
                    money_amt = money_amt * 0.5
                    print("Total amount: ", money_amt)
                elif now_hour >= 8 and now_hour < 16:
                    print("You will get 10% discount from your car park payment.")
                    money_amt = money_amt * 0.9
                    print("Total amount: ", money_amt)
            else:
                print("Your frequent parking number is invalid.")
                print("Your total, the original total,: ", money_amt)

        dailyPayments(now_hour, dailyCarsPayTotal, money_amt)

    def morningCarPark(hour_duration, today_date):
        if today_date >= 0 and today_date <= 4:
            if hour_duration > 2:
                print("You cannot park your car for more than 2hrs. Sorry!")
            else:
                carPark_payment = 10.00 * hour_duration
                print("Your total payment: ", carPark_payment)
                money_amt = carPark_payment
                freqParkNumDiscount(money_amt, now_hour)

        elif today_date == 5:
            if hour_duration > 4:
                print("You cannot park your car for more than 4hrs. Sorry!")
            else:
                carPark_payment = 3.00 * hour_duration
                print("Your total payment: ", carPark_payment)
                money_amt = carPark_payment
                freqParkNumDiscount(money_amt, now_hour)


    def morn_eveCarPark(now_hour, today_date):
        if today_date >= 0 and today_date <= 4:
            morning_time_payment = (16 - now_hour) * 10.00
            evening_time_payment = 2.00
            carPark_payment = morning_time_payment + evening_time_payment
            print("Your total payment: ", carPark_payment)
            money_amt = carPark_payment
            freqParkNumDiscount(money_amt, now_hour)

        elif today_date == 5:
            morning_time_payment = (16 - now_hour) * 3.00
            evening_time_payment = 2.00
            carPark_payment = morning_time_payment + evening_time_payment
            print("Your total payment: ", carPark_payment)
            money_amt = carPark_payment
            freqParkNumDiscount(money_amt, now_hour)

        elif today_date == 6:
            morning_time_payment = (16 - now_hour) * 2.00
            evening_time_payment = 2.00
            carPark_payment = morning_time_payment + evening_time_payment
            print("Your total payment: ", carPark_payment)
            money_amt = carPark_payment
            freqParkNumDiscount(money_amt, now_hour)


    def eveningCarPark():
        leave_hour = float(input("Enter time you want to leave: "))
        import math
        leave_hour1 = math.floor(leave_hour)

        if leave_hour1 > 0 and leave_hour1 <= 16:
            print("You cannot park your car beyond midnight. Sorry!")
        elif leave_hour1 > 16 and (leave_hour1 <= 23 or leave_hour1 == 24):
            carPark_payment = 2.00
            print("Your total payment: ", carPark_payment)
            money_amt = carPark_payment
            freqParkNumDiscount(money_amt, now_hour)

        elif now_hour >= 0 and now_hour < 8:
            print("You cannot park your car from midnight till 8 am. Sorry!")


    def weekdaysPark(now_hour, today_date):
        if now_hour >= 8 and now_hour < 16:
            leave_hour = float(input("Enter time you want to leave: "))
            import math
            leave_hour1 = math.floor(leave_hour)

            hour_duration = leave_hour1 - now_hour
            if (now_hour >= 8 and now_hour <= 13):
                morningCarPark(hour_duration, today_date)
            elif (now_hour > 13 and now_hour <= 15):
                if leave_hour1 == 16:
                    morningCarPark(hour_duration, today_date)
                elif leave_hour1 > 16 and leave_hour1 <= 24:
                    morn_eveCarPark(now_hour, today_date)
        elif (now_hour >= 16 and now_hour < 24):
            eveningCarPark()
        elif now_hour == 24 or (now_hour >= 1 and now_hour < 8):
            print("You cannot park your car from midnight till 8 am. Sorry!")


    def SaturdayCarPark(now_hour, today_date):
        if now_hour >= 8 and now_hour < 16:
            leave_hour = float(input("Enter time you want to leave: "))
            import math
            leave_hour1 = math.floor(leave_hour)

            hour_duration = leave_hour1 - now_hour
            if (now_hour >= 8 and now_hour <= 11):
                morningCarPark(hour_duration, today_date)
            elif (now_hour > 11 and now_hour <= 15):
                if leave_hour1 == 16:
                    morningCarPark(hour_duration, today_date)
                elif leave_hour1 > 16:
                    morn_eveCarPark(now_hour, today_date)
        elif (now_hour >= 16 and now_hour < 24):
            eveningCarPark()
        elif now_hour == 24 or (now_hour >= 1 and now_hour < 8):
            print("You cannot park your car from midnight till 8 am. Sorry!")

    def SundayCarPark(now_hour, today_date):
        if now_hour >= 8 and now_hour < 16:
            leave_hour = float(input("Enter time you want to leave: "))
            import math
            leave_hour1 = math.floor(leave_hour)

            if leave_hour1 <= 16:
                hour_duration = leave_hour1 - now_hour
                carPark_payment = 2.00 * hour_duration
                print("Your total payment: ", carPark_payment)
                money_amt = carPark_payment
                freqParkNumDiscount(money_amt, now_hour)
            elif leave_hour1 > 16:
                morn_eveCarPark(now_hour, today_date)

        elif (now_hour >= 16 and now_hour < 24):
            eveningCarPark()
        elif now_hour == 24 or (now_hour >= 1 and now_hour < 8):
            print("You cannot park your car from midnight till 8 am. Sorry!")


    from datetime import date
    import calendar
    my_date = date.today()
    today_day = "Today is " + calendar.day_name[my_date.weekday()]
    print(today_day)

    import datetime
    datetime.datetime.today()
    today_date = datetime.datetime.today().weekday()

    from time import localtime
    stobj = localtime()
    now_hour = stobj.tm_hour
    if now_hour == 0:
        now_hour = 24
    now_hour1 = "Hour now: " + str(now_hour)
    print(now_hour1)


    while validity == False:
        userCar = userCar + 1
        print("Car no.",userCar)
        userCarinput = str(input("Do you want to park your car?: "))
        if userCarinput.lower() == "no" or userCarinput.lower() == "n":
            validity = True
            exit()
        elif userCarinput.lower() == "yes" or userCarinput.lower() == "y":
            # today_date = int(input("Enter today's date: "))
            # now_hour = int(input("Enter the hour now: "))

            if now_hour == 24 or (now_hour >= 1 and now_hour <= 7):
                print("You cannot park your car from midnight till 8am. Sorry!")
                dailyPayments(now_hour, dailyCarsPayTotal, money_amt)
                exit()
            else:
                if today_date >= 0 and today_date <= 4:
                    weekdaysPark(now_hour, today_date)
                elif today_date == 5:
                    SaturdayCarPark(now_hour, today_date)
                elif today_date == 6:
                    SundayCarPark(now_hour, today_date)

    if now_hour == 24:
        dailyPayments(now_hour, dailyCarsPayTotal, money_amt)


global userCar
global dailyCarsPayTotal
userCar = 0
dailyCarsPayTotal = 0
dayCarPark(userCar, dailyCarsPayTotal)
