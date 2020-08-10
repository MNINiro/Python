Surname = input("Key in Surname ")
SLength = len(Surname)
CustomerID = 0

for i in range(SLength):
# NextChar is a single character from surname
       NextChar = Surname[i]
       NextCodeNumber = ord(NextChar)
       CustomerID = CustomerID + NextCodeNumber
       print("Customer ID is " + str(CustomerID))
