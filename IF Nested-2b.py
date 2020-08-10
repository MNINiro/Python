group= (input("Enter group (Student/Teacher) :"))


if group=="Student":
        Name= (input("Enter Name :"))
        if Name=="Atif":
           print ("valid student")
        else:
           print("invalid student")

elif group=="Teacher":
        Name= (input("Enter Name :"))
        if Name=="Khalid":
           print ("valid teacher")
        else:
           print ("invalid teacher name")
else:
    print ("invalid group")
