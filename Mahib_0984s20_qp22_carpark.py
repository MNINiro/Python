day = None

while day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday'):

    day = str(input("Enter day: ")).lower()

    if day in ('monday','tuesday','wednesday','thursday','friday'):

        arrival = None

        while arrival not in (8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23):
            arrival = int(input("Enter the hour of arrival: "))

            if (8 <= arrival <= 15):
                price_per_hour = 10

                hour = None
                while hour not in (1,2):
                    hour = int(input("Enter the number of hours for your parking: "))

                    if ((1 <= hour <= 2) == False):
                        print("Not a valid option.")

                    if (arrival + hour) >= 16:
                        hour = 16 - arrival
                        price = hour * price_per_hour + 2

                    else:
                        price = hour * price_per_hour

            elif (16 <= arrival <= 23):
                price = 2

            else:
                print("Not an available timing.")

    elif day in ('sunday','saturday'):

        arrival = None

        while arrival not in (8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23):
            arrival = int(input("Enter the hour of arrival: "))

            if day == 'sunday':
                if (8 <= arrival <= 15):
                    price_per_hour = 2

                    hour = None
                    while hour not in (1,2,3,4,5,6,7,8):
                        hour = int(input("Enter the number of hours for your parking: "))

                        if (arrival + hour) >= 16:
                            hour = 16 - arrival
                            price = hour * price_per_hour + 2

                        else:
                            price = hour * price_per_hour

                        if ((1 <= hour <= 8) == False):
                            print("Not a valid option.")



                elif (16 <= arrival <= 23):
                    price = 2

                else:
                    print("Not an available timing.")

            elif day == 'saturday':
                if (8 <= arrival <= 15):
                    price_per_hour = 3

                    hour = None
                    while hour not in (1,2,3,4):
                        hour = int(input("Enter the number of hours for your parking: "))

                        if ((1 <= hour <= 4) == False):
                            print("Not a valid option.")

                        if (arrival + hour) >= 16:
                            hour = 16 - arrival
                            price = hour * price_per_hour + 2

                elif (16 <= arrival <= 23):
                    price = 2

                else:
                    print("Not an available timing.")

    else:
        print("Not a valid day.")

print(f"Your current price is ${price}.")




discount_verification = False
parking_number_cd = []
frequent_number = []

input_number = str(input("Do you have a frequent parking number? (y/n): ")).lower()


while(input_number == 'y'):

    frequent_parking_number = '1235'


    while (len(frequent_parking_number) != 5):
        frequent_parking_number = str(input("Enter your frequent parking number (5 digits): "))


        if (len(frequent_parking_number) == 5):
            for i in range(5):
                parking_number_cd.append(int(frequent_parking_number[i]))
                frequent_number.append(int(frequent_parking_number[i]))
                i += 1
            parking_number_cd.pop(4)
            input_number = 'n'
            discount_verification = True

        elif (len(frequent_parking_number) != 5):
            print('Not a valid format.')


def checkdigit(lst):
    j = 6
    tot = 0

    for i in range(len(lst)):
        j -= 1  # j = j-1
        tot += lst[i] * j
    rmd = tot % 11
    cd = 11 - rmd
    parking_number_cd.append(cd)

checkdigit(parking_number_cd)

if discount_verification == True:
    correct_number = 10000*(parking_number_cd[0]) + 1000*(parking_number_cd[1]) + 100*(parking_number_cd[2]) + 10*(parking_number_cd[3]) + parking_number_cd[4]
    correct_number = str(correct_number)

    if correct_number == frequent_parking_number:
        if 16 <= arrival <= 23:
            discount = 50/100 * price
            discount_price = price - discount
            print("Your discount is 50%.")
            print(f"Your total parking fees: ${discount_price}")

        elif 8 <= arrival <= 15:
            discount = 10/100 * price
            discount_price = price - discount
            print("Your discount is 10%.")
            print(f"Your total parking fees: ${discount_price}")

        else:
            discount_price = price
            print(f"Your total parking fees: ${discount_price}")
    else:
        print("Your frequent parking number is not valid.")
        print(f"Your total parking fees: ${price}")
else:
    print(f"Your total parking fees: ${price}")
