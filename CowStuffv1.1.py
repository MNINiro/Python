import math
cowID=[]
while True:
    cowID.append(int(input("Enter the identity code :")))
    end=input("Is that all your cows ? Enter ""Y"" for Yes and ""N"" for No")
    if end=="y":
        break
milk=[[ 0 for x in range(15)] for y in range(len(cowID))]
for i in range (len(cowID)):
    milk[i][0]=cowID[i]
print(milk)
for day in range(1,3):
    while True :
        cowname=int(input("Enter the cow's ID :"))
        if cowname in cowID:
            cowmilknow=int(input("Enter the litres of milk milked :"))
            for i in range(len(cowID)) :
                if cowname==cowID[i] :
                    milk[i][day]=milk[i][day]+cowmilknow
        else :
            print("No such cow !")
        print(milk)
        end=input("Is the day milking over nibba ? ")
        if end=="y":
            break
    while True :
        cowname=int(input("Enter the cow's ID :"))
        if cowname in cowID :
            cowmilknow=int(input("Enter the litres of milk milked :"))
            for i in range(len(cowID)) :
                if cowname==cowID[i] :
                    milk[i][day+7]=milk[i][day+7]+cowmilknow
        else :
            print("No such cow !")
        print(milk)
        end=input("Is the day over nibba ? ")
        if end=="y":
            break
milkstat=[[ 0 for x in range(3)] for y in range(len(cowID))]
for i in range (len(cowID)):
    milkstat[i][0]=cowID[i]
print(milkstat)
#tot
for i in range (len(cowID)):
    for j in range (1,8):
        milkstat[i][1]=milkstat[i][1]+milk[i][j]+milk[i][j+7]
#rounding
for i in range (len(cowID)):
    for j in range (1,8):
        milkstat[i][1]=round(milkstat[i][1],0)
print(milkstat)
#avg
for i in range (len(cowID)):
    for j in range (1,8):
        milkstat[i][2]=round(milkstat[i][1]/7,0)
print(milkstat)
high=[]
low=[]
highconst=int()
for i in range(len(cowID)):
    if milkstat[i][1]>=highconst:
        highconst=milkstat[i][1]
    if milkstat[i][1]<48:
        low.append(cowID[i])
for i in range(len(cowID)):
    if milkstat[i][1]==highconst:
        high.append(cowID[i])
print("The highest milk producers are:",high,"\n The lowest milk producers are",low)

