middayTemp = []
midnightTemp = []

for day in range(3):
    mdt = int(input('Enter mid day temperature:'))
    if (mdt < 25) or (mdt > 35):
        print('Invalid day temperature')
    else:
        middayTemp.append(mdt)

    mnt = int(input('Enter mid night temperature:'))
    if (mnt < 15) or (mnt > 30):
        print('Invalid night temperature')
    else:
        midnightTemp.append(mnt)

print('Mid Day Temp:', middayTemp)
print('Mid night Temp:', midnightTemp)

totalDayTemp = 0
totalNightTemp = 0

for i in range(len(middayTemp)):
    totalDayTemp += middayTemp[i]
    totalNightTemp += midnightTemp[i]

avgDayTemp = totalDayTemp / len(middayTemp)
avgNightTemp = totalNightTemp / len(midnightTemp)

print('Average Day Temp:', avgDayTemp)
print('Average Night Temp:', avgNightTemp)

maxDayTemp = 0

for j in middayTemp:
    if j > maxDayTemp:
        maxDayTemp = j
print('Maximum Day Temp:', maxDayTemp, 'in day', (middayTemp.index(maxDayTemp)) + 1)

minNightTemp = 30
for k in midnightTemp:
    if k < minNightTemp:
        minNightTemp = k
print('Minimum Night Temp:', minNightTemp, 'in day', (midnightTemp.index(minNightTemp)) + 1)
