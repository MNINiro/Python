ServiceTime = 30
planeType = []
flightLength = []

for i in range(0,3):
    x = str(input("Enter type of plane 2S/4S/HP: "))
    x = x.upper()
    while (x != '2S') and (x != '4S') and (x != 'HP'): #for validation
        print('Invalid Plane type!!!')
        x = str(input('Enter Plane Type:'))
        x = x.upper()
    else:
        planeType.append(x)
        print(planeType)
print(planeType, "are the types of planes available.")

for i in range(0,2):
    y = int(input("Enter length of flight: "))
    while (y != 30) and (y != 60):
        print('Invalid flying time entered!')
        y = int(input("Enter length of flight: "))
    else:
        flightLength.append(y)
        print(flightLength)
print(flightLength, "are the length of flights available.")

for i in range(0,2):
    if flightLength[i] == 30:
        perFlightTime = flightLength[i] + ServiceTime
        dailyMinutes = 10 * 60
        numberOfFlights = int(dailyMinutes/perFlightTime)
        print(f"The maximum number of flights is {numberOfFlights}")

        if '2S' in planeType:
            PerFlight = 100
            income = numberOfFlights * PerFlight
            print('for 2S:',income)
        if '4S' in planeType:
            PerFlight = 120
            income = numberOfFlights * PerFlight
            print('for 4S',income)
        if 'HP' in planeType:
            PerFlight = 300
            income = numberOfFlights * PerFlight
            print('for HP:',income)

    elif flightLength[i] == 60:
        perFlightTime = flightLength[i] + ServiceTime
        dailyMinutes = 10 * 60
        numberOfFlights = int(dailyMinutes / perFlightTime)
        print(f"The maximum number of flights is {numberOfFlights}")

        if '2S' in planeType:
            PerFlight = 150
            income = numberOfFlights * PerFlight
            print('Income from 2S:',income)
        if '4S' in planeType:
            PerFlight = 200
            income = numberOfFlights * PerFlight
            print('Income from 4S',income)
        if 'HP' in planeType:
            PerFlight = 500
            income = numberOfFlights * PerFlight
            print('Income from HP:',income)
    else:
        print("The length entered is invalid.")

