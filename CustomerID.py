# Surname String
# NextChar Char
# NextCodeNumber, I, CustomerID, SLength Integer

##Surname = input("Key in Surname ")
##SLength = len(Surname)
##CustomerID = 0
##for i in range(SLength):
##    # NextChar is a single character from surname
##    NextChar = Surname[i]
##    NextCodeNumber = ord(NextChar)
##    CustomerID = CustomerID + NextCodeNumber
##    print("Customer ID is " + str(CustomerID))
##

NextCodeNumber=[]


def encrypt(Sname):
    x = ""
    SLength = len(Sname)
    print(Sname)

    for i in range(SLength):
        NextChar = Sname[i]
        OrdChar = ord(NextChar)

        x = x + chr(OrdChar+1)
    print(x)

##        NextCodeNumber.append(chr(OrdChar+1))
##    print(NextCodeNumber)
        
        
encrypt('Niro')
