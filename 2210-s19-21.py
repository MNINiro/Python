Days = []
BusA = []
BusB = []
BusC = []
BusD = []
BusE = []
BusF = []
LateDays = []
AvgLtTime = []

def validateTime(minutes):
    if minutes < -10 or minutes > 10:
        print('invalid minutes entered')
    else:
        return minutes

for dy in range(2):
    d = input("Enter Day (i.e. Mon1) :")
    Days.append(d)

    bA = int(input("Enter arrival time of BusA:"))
    A = validateTime(bA)
    BusA.append(A)


    bB = int(input("Enter arrival time of BusB:"))
    B = validateTime(bB)
    BusB.append(B)

    bC = int(input("Enter arrival time :"))
    C = validateTime(bC)
    BusC.append(C)

    bD = int(input("Enter arrival time :"))
    D = validateTime(bD)
    BusD.append(D)

    bE = int(input("Enter arrival time :"))
    E = validateTime(bE)
    BusE.append(E)

    bF = int(input("Enter arrival time :"))
    F = validateTime(bF)
    BusF.append(F)


for dy in range(1):
    print("Days :", Days)
    print("BusA :", BusA)
    print("BusB :", BusB)
    print("BusB :", BusC)
    print("BusB :", BusD)
    print("BusB :", BusE)
    print("BusB :", BusF)

# LatADays = 0
# for ld in range(2):
#     if BusA[i] < 0:
#         lateADays += 1
