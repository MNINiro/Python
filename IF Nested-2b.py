group= (input("Enter group (Student/Teacher) :"))
group = group.upper()
if group=="STUDENT":
        Name= (input("Enter Name :"))
        Name = Name.upper()
        if Name=="ATIF":
           print ("valid student")
        else:
           print("invalid student")

elif group=="TEACHER":
        Name= (input("Enter Name :"))
        Name = Name.upper()
        if Name=="KHALID":
           print ("valid teacher")
        else:
           print ("invalid teacher name")
else:
    print ("invalid group")
