## --------------Task 1-----------------------------##

def Comp_Shop_List():
    Comp_Parts_ListFile = open("Computer Parts List.txt", "r")
    for i in range(0, 13):
        record = Comp_Parts_ListFile.readline()
        print(record)
    Comp_Parts_ListFile.close()


def Comp_Cost_Add():
    Buyer_Info = open("Buyer_PurchaseInfo.txt", "w+")
    Buyer_Info.write("Computer Price:" + "       " + str(200))
    Buyer_Info.close()


def Customer_Record_Output(y):
    Buyer_Info = open("Buyer_PurchaseInfo.txt", "a+")
    Buyer_Info.write("\nTotal:" + "  " + str(y))
    Buyer_Info.close()

    Buyer_Info = open("Buyer_PurchaseInfo.txt", "r")
    for a in range(0, 10):
        record1 = Buyer_Info.readline()
        print(record1)
    Buyer_Info.close()


def Comp_Shop_List1(x):
    Comp_Parts_ListFile = open("Computer Parts List.txt")
    BuyerData = open("Buyer_PurchaseInfo.txt", "a+")

    record = Comp_Parts_ListFile.readlines()
    if x == "A1":
        BuyerData.write("\nCase:" + "     " + record[1])
    elif x == "A2":
        BuyerData.write("\nCase:" + "     " + record[2])
    elif x == "B1":
        BuyerData.write("\nRAM:" + "     " + record[5])
    elif x == "B2":
        BuyerData.write("\nRAM:" + "     " + record[6])
    elif x == "B3":
        BuyerData.write("\nRAM:" + "     " + record[7])
    elif x == "C1":
        BuyerData.write("\nMain HDD:" + "     " + record[10])
    elif x == "C2":
        BuyerData.write("\nMain HDD:" + "     " + record[11])
    elif x == "C3":
        BuyerData.write("\nMain HDD:" + "     " + record[12])

    Comp_Parts_ListFile.close()
    BuyerData.close()


def Case_BuyValid(Total_BuyAmt):
    valid = False
    code_list = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]

    while valid == False:
        userCase_choice = str(input("Enter item code of the case you want to buy: "))
        for i in range(2, len(code_list)):
            if userCase_choice == code_list[i]:
                print("You have entered a wrong item code for the case item. Please try again.")
                break

        if userCase_choice == "A1":
            Total_BuyAmt1 = Total_BuyAmt + 75.00
            Comp_Cost_Add()
            Comp_Shop_List1(userCase_choice)

            valid = True
            return Total_BuyAmt1


        elif userCase_choice == "A2":
            Total_BuyAmt1 = Total_BuyAmt + 150.00
            Comp_Cost_Add()
            Comp_Shop_List1(userCase_choice)

            valid = True
            return Total_BuyAmt1


        else:
            print("No such item code exists.")


def RAM_BuyValid(Total_BuyAmt1):
    valid = False
    code_list = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]

    while valid == False:
        userRAM_choice = str(input("Enter item code of the RAM you want to buy: "))

        for i in range(5, len(code_list)):
            if userRAM_choice == code_list[i]:
                print("You have entered a wrong item code for the RAM item. Please try again.")
                break

        if userRAM_choice == "B1":
            Total_BuyAmt2 = Total_BuyAmt1 + 79.99
            Comp_Shop_List1(userRAM_choice)
            valid = True
            return Total_BuyAmt2


        elif userRAM_choice == "B2":
            Total_BuyAmt2 = Total_BuyAmt1 + 149.99
            Comp_Shop_List1(userRAM_choice)
            valid = True
            return Total_BuyAmt2


        elif userRAM_choice == "B3":
            Total_BuyAmt2 = Total_BuyAmt1 + 299.99
            Comp_Shop_List1(userRAM_choice)
            valid = True
            return Total_BuyAmt2


        elif userRAM_choice == "A1" or userRAM_choice == "A2":
            print("You cannot buy anymore cases.")

        else:
            print("No such code exists.")


def MainHDD_BuyValid(Total_BuyAmt2):
    valid = False
    code_list = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]

    while valid == False:
        userMainHDD_choice = str(input("Enter item code of the Main Hard Disc you want to buy: "))

        for i in range(8, len(code_list)):
            if userMainHDD_choice == code_list[i]:
                print("You have entered a wrong item code for the Main Hard Disc item. Please try again.")
                break

        if userMainHDD_choice == "C1":
            Total_BuyAmt3 = Total_BuyAmt2 + 49.99
            Comp_Shop_List1(userMainHDD_choice)
            valid = True
            return Total_BuyAmt3

        elif userMainHDD_choice == "C2":
            Total_BuyAmt3 = Total_BuyAmt2 + 89.99
            Comp_Shop_List1(userMainHDD_choice)
            valid = True
            return Total_BuyAmt3


        elif userMainHDD_choice == "C3":
            Total_BuyAmt3 = Total_BuyAmt2 + 129.99
            Comp_Shop_List1(userMainHDD_choice)
            valid = True
            return Total_BuyAmt3

        elif userMainHDD_choice == "A1" or userMainHDD_choice == "A2":
            print("You cannot buy anymore cases.")

        elif userMainHDD_choice == "B1" or userMainHDD_choice == "B2" or userMainHDD_choice == "B3":
            print("You cannot buy anymore RAM.")

        else:
            print("No such code exists.")


Total_BuyAmt = 0.00
Total_BuyAmt1 = 0.00
Total_BuyAmt2 = 0.00
Total_BuyAmt3 = 0.00
global userCase_choice

print("Hello, Welcome to our Online Computer Shop \nFor each computer you buy, you have to pay $200 for its basic components.")
user_option1 = input("Do you want to buy a computer: ")

if user_option1.lower() == "no":
    print("We are sorry to see you go. See you next time!")
    exit()


else:
    Total_BuyAmt = Total_BuyAmt + 200
    print("Now you HAVE to buy ONLY 1 RAM, 1 Case, and 1 Main Hard drive for your computer.")
    Comp_Shop_List()

    Total_BuyAmt1 = Case_BuyValid(Total_BuyAmt)
    Total_BuyAmt2 = RAM_BuyValid(Total_BuyAmt1)
    Total_BuyAmt3 = MainHDD_BuyValid(Total_BuyAmt2)

    Customer_Record_Output(Total_BuyAmt3)

## -------------- End of Task 1 --------------------##


## ------------- Task 2 --------------------------- ##

def Comp_Shop_List4(x):
    Comp_Parts_ListFile = open("Computer Parts List.txt")
    BuyerData = open("Buyer_PurchaseInfo.txt", "a+")

    record = Comp_Parts_ListFile.readlines()
    if x == "D1":
        BuyerData.write("\nSolid State Drive:" + "     " + record[15])
    elif x == "D2":
        BuyerData.write("\nSolid State Drive:" + "     " + record[16])
    elif x == "E1":
        BuyerData.write("\nSecond Hard Disk Drive:" + "     " + record[19])
    elif x == "E2":
        BuyerData.write("\nSecond Hard Disk Drive:" + "     " + record[20])
    elif x == "E3":
        BuyerData.write("\nSecond Hard Disk Drive:" + "     " + record[21])
    elif x == "F1":
        BuyerData.write("\nOptical Drive:" + "     " + record[24])
    elif x == "F2":
        BuyerData.write("\nOptical Drive:" + "     " + record[25])
    elif x == "G1":
        BuyerData.write("\nOperating System:" + "     " + record[28])
    elif x == "G2":
        BuyerData.write("\nOperating System:" + "     " + record[29])
    else:
        BuyerData.write("\nSecond Total:"+"  "+str(x))

    Comp_Parts_ListFile.close()
    BuyerData.close()

def Customer_Record_Output1():
    Buyer_Info = open("Buyer_PurchaseInfo.txt", "r")
    record1 = Buyer_Info.read()
    print(record1)
    Buyer_Info.close()


def Additional_PartsFunc(h):
    global Total_BuyAmt4
    global valid1
    while valid1 == False:
        buyerChoice = str(input("Type in the item code of the components that you want to purchase: "))
        code_list = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]
        for c in range(0,8):
            if buyerChoice == code_list[c]:
                print("Sorry, but you cannot buy more than 1 Case, RAM or Main Hard Disc")

        if buyerChoice == "D1":
            Total_BuyAmt4 = h + 59.99
            Comp_Shop_List4(buyerChoice)
            user_MultiplePurchase()
            return Total_BuyAmt4

        elif buyerChoice == "D2":
            Total_BuyAmt4 = h + 119.99
            Comp_Shop_List4(buyerChoice)
            user_MultiplePurchase()
            return Total_BuyAmt4

        elif buyerChoice == "E1":
            Total_BuyAmt4 = h + 49.99
            Comp_Shop_List4(buyerChoice)
            user_MultiplePurchase()
            return Total_BuyAmt4

        elif buyerChoice == "E2":
            Total_BuyAmt4 = h + 89.99
            Comp_Shop_List4(buyerChoice)
            user_MultiplePurchase()
            return Total_BuyAmt4

        elif buyerChoice == "E3":
            Total_BuyAmt4 = h + 129.99
            Comp_Shop_List4(buyerChoice)
            user_MultiplePurchase()
            return Total_BuyAmt4

        elif buyerChoice == "F1":
            Total_BuyAmt4 = h + 50.00
            Comp_Shop_List4(buyerChoice)
            user_MultiplePurchase()
            return Total_BuyAmt4

        elif buyerChoice == "F2":
            Total_BuyAmt4 = h + 100.00
            Comp_Shop_List4(buyerChoice)
            user_MultiplePurchase()
            return Total_BuyAmt4

        elif buyerChoice == "G1":
            Total_BuyAmt4 = h + 100.00
            Comp_Shop_List4(buyerChoice)
            user_MultiplePurchase()
            return Total_BuyAmt4

        elif buyerChoice == "G2":
            Total_BuyAmt4 = h + 175.00
            Comp_Shop_List4(buyerChoice)
            user_MultiplePurchase()

        else:
            print("No such item code exists")



def user_MultiplePurchase():
    global valid1
    user_option = str(input("Do you want to buy any more components?: "))
    if user_option.lower()=="y" or user_option.lower()=="yes":
        valid1 = False
        Additional_PartsFunc(Total_BuyAmt4)

    elif user_option.lower()=="n" or user_option.lower()=="no":
        print("Thanks for shopping here at our Online Computer Shop! Hope you have a nice day!")
        valid1 = True
        Comp_Shop_List4(Total_BuyAmt4)
        Customer_Record_Output1()

    else:
        print("Invalid Data. Try again")
        user_MultiplePurchase()


def Comp_Shop_List3():
    Comp_AdditionParts_File = open("Computer Parts List.txt","r")
    record = Comp_AdditionParts_File.readlines()
    print(record[13:30])

    Comp_AdditionParts_File.close()

valid1 = False
Total_BuyAmt4 = float(Total_BuyAmt3)
print("Hello.\nNow that you have bought the basic mandatory parts of your computer, do you want to buy any other items?")
user_Option1 = str(input("Enter 'yes' to buy additional parts, and if you don't want to, enter 'no': "))
if user_Option1.lower() == "n" or user_Option1.lower() == "no":
    print("Thanks for shopping here at our Online Computer Shop! Hope you have a nice day!")
else:
    Comp_Shop_List3()
    Additional_PartsFunc(Total_BuyAmt4)


## -------------------- End of Task 2 ------------------------------ ##