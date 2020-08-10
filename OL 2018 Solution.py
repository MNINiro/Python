
#Recording the yield
Cow = []
Yield = []
 
Cows = int(input("How many cows are in the herd?  "))
Day = 0     #to configure the milking
for i in range(14):
    if i%2 == 1:
        Milking = "Second"
    else:
        Milking = "First"
        Day += 1
    print("Day ", Day, "; ", Milking, " milking")
    for i in range(Cows):
        while True:
            Code = int(input("Enter code: "))
            if Code > 999 or Code < 100:
                print("Enter a 3-digit code please")
            else:
                Cow.append(Code)
                break
        Y = float(input("Enter volume of milk in litres: "))    #A range check for yield can be added 
        Yield.append(Y)

#Task 2

#Finding the Total and Average
Total = 0
for i in range(len(Yield)):
    Total += Yield[i]
Average = Total/Cows
 
round(Total, 0)
round(Average, 0)
 
print("Total weekly volume of milk: ", int(Total), " litres")
print("Average yield per cow: ", int(Average), " litres")


#Task 3

#Identifying most productive and low producing cows

Total = []
LessMilk = ""
YieldOnDay = 0
Milking = 0
for j in range(Cows):
    T = 0
    Days = 0
    Cow = Cow[j]                    #A cow chosen 
    for i in range(len(Cow)):
        if Cow[i] == Cow:
            T += Yield[i]         #Incrementing the total for each cow 
            YieldOnDay += Yield[i]
            Milking += 1
            if Milking == 2:            # 2 since checking for days, not milkings
                if YieldOnDay < 12: #Checking if yield is less than 12 Days += 1 Milking = 0 YieldOnDay = 0 if Days > 3:        #Low yield for 4 or more days 
                    LessMilk = LessMilk + str(Cow[j]) + ", "
    Total.append(T)
 
print(Total)
for i in range(len(Cows)):
    if Total[i] == max(Total):
        print("Cow ", Cow[i], " has the highest yield of ", Total[i], " litres")
 
print("Cows which produced less than 12 litres of milk: " , LessMilk)


