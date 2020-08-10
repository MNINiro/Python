#Task 1 ---------------------------------------------------------------------------------------------

Days = []
BusA = []
BusB = []
LateDays = []

for dy in range(2):
    d = input("Enter Day: ")
    bA = int(input("Enter arrival time of BusA: "))
    bB = int(input("Enter arrival time of BusB: "))

    Days.append(d)
    BusA.append(bA)
    BusB.append(bB)

print(f"Days: {Days}")
print(f"BusA: {BusA}")
print(f"BusB: {BusB}")

#Task 2 -----------------------------------------------------------------------------------------------------------

LateADays = 0
LateBDays = 0

for lb in BusA:
    if lb < 0:
        LateADays += 1

for lb in BusB:
    if lb < 0:
        LateBDays += 1

print(f'Number of bus(es) late in route BusA: {LateADays}.')
print(f'Number of bus(es) late in route BusB: {LateBDays}.')

def sumNegativeA(BusA):
    sum = 0
    for initialLt in BusA:
        if initialLt < 0:
            sum += initialLt
    return sum

print(f'The average number of minutes late for BusA route is {-sumNegativeA(BusA)/LateADays} minute(s).')

def sumNegativeB(BusB):
    sum = 0
    for initialLt in BusB:
        if initialLt < 0:
            sum += initialLt
    return sum

print(f'The average number of minutes late for BusB route is {-sumNegativeB(BusB)/LateBDays} minute(s).')

if LateADays > LateBDays:
    print('BusA route had the highest number of buses late.')
elif LateBDays > LateADays:
    print('BusB route had the highest number of buses late.')
else:
    print("Both routes had the same number of buses late.")

#Task 3 -------------------------------------------------------------------------------------------------------

inputD = input("Enter the day you want to be analysed: ")

if inputD == Days[0]:
    print(f'The timings for your inquired day: {BusA[0]} and {BusB[0]}')
    print(f'{LateADays} buses were late on this particular day.')
    for lb in BusA:
        if BusA[0] < 0:
            print(f'This bus was late {-BusA[0]} minutes using route BusA.')
        if BusA[1] < 0:
            print(f'This bus was late {-BusA[1]} minutes using route BusA.')
        break

if inputD == Days[1]:
    print(f'The timings for your inquired day: {BusA[1]} and {BusB[1]}')
    print(f'{LateBDays} bus(es) were late on this particular day.')
    for lb in BusB:
        if BusB[0] < 0:
            print(f'This bus was late {-BusB[0]} minutes using route BusB.')
        if BusB[1] < 0:
            print(f'This bus was late {-BusB[1]} minutes using route BusB.')
        break

