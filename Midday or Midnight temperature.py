#Task 1 -----------------------------------------------------------------------
nDays = int(input("Enter the number of days: "))
dayTemp = []
nightTemp = []

for days in range(nDays):
    dt = float(input("Enter Midday temperature: "))
    
    while True:
        if (dt < 17) or (dt > 40):
               print("Error! Please enter temperature between 17 and 40 degree")
               dt = float(input("Enter Midday temperature: "))
        else:
            dayTemp.append(dt)
            break           
           
    nt = float(input("Enter Midnight temperature: "))

    while True:
        if (nt < 17) or (nt > 40):
               print("Error! Please enter temperature between 17 and 40 degree")
               nt = float(input("Enter Midnight temperature: "))
        else:
            nightTemp.append(nt)
            break   

print(dayTemp)
print(nightTemp)

#Task 2 ------------------------------------------------------------------------
Dtemp = 0
Ntemp = 0

for i in range(nDays):
    Dtemp += dayTemp[i]
    Ntemp += nightTemp[i]

avgDT = Dtemp/nDays
avgNT = Ntemp/nDays

print (f'The average temperature in the day time is {avgDT} degrees.')
print (f'The average temperature in the night time is {avgNT} degrees.')

#Task 3 ------------------------------------------------------------------------

maxTemp = float(max(dayTemp))
minTemp = float(min(nightTemp))

print(f"The maximum temperature is {maxTemp} in day number {int(dayTemp.index(maxTemp))+1}.")
print(f"The minimum temperature is {minTemp} in day number {int(nightTemp.index(minTemp))+1}.")
