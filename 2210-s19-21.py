Days=[]
BusA = []
BusB = []
BusC = []
BusD = []
BusE = []
BusF = []
LateDays = []
AvgLtTime = []

for dy in range(2):
    d = input("Enter Day (i.e. Mon1) :")
    bA = input("Enter arrival time of BusA:")
    bB = input("Enter arrival time of BusB:")
##    bC = input("Enter arrival time :")
##    bD = input("Enter arrival time :")
##    bE = input("Enter arrival time :")
##    bF = input("Enter arrival time :")

    Days.append(d)
    BusA.append(bA)
    BusB.append(bB)
##    BusC.append(bC)
##    BusD.append(bD)
##    BusE.append(bE)
##    BusF.append(bF)
    
##for dy in range(2):
print("Days :", Days)
print("BusA :", BusA)
print("BusB :", BusB)

LatADays = 0
for ld in range(2):
    if BusA[i] < 0:
        lateADays += 1
