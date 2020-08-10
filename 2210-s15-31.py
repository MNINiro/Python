dayTemp = []
nightTemp = []

for days in range(2):

    dt = float(input("Enter Midday temperature :"))

    while True:
        if (dt < 17) or (dt > 40):
               print("Error! Please enter temperature in between 17 and 40 degree")
               dt = float(input("ReEnter Midday temperature :"))
        else:
            dayTemp.append(dt)
            break

    nt = float(input("Enter Midnight temperature :"))
    
    while True:     
        if (nt < 17) or (nt > 40):
            print("Error! Please enter temperature in between 17 and 40 degree")
            nt = float(input("ReEnter Midnight temperature :"))          
        else:
            nightTemp.append(nt)
            break

print(dayTemp)
print(nightTemp)

Dtemp = 0
Ntemp = 0

for i in range(2):
    Dtemp += dayTemp[i]
    Ntemp += nightTemp[i]
