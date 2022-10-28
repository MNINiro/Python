group= (input("Enter group (Student/Teacher/Admin) :"))
group = group.upper()

if group=="STUDENT":
        Name= input("Enter student Name :")
        Name = Name.upper()
        stdNm = ['ATIF','AKRAM','MUDASSIR']
        if Name in stdNm:
           print ("valid student")
        else:
           print("invalid student")

elif group=="TEACHER":
        Name= input("Enter teacher Name :")
        Name = Name.upper()
        if Name == "KHALID":
           print ("valid teacher")
        else:
           print ("invalid teacher name")

if group=="ADMIN":
        Name= input("Enter Admin person Name:")
        Name = Name.upper()

        AdmnNm = ['CHAMAN','SHARMIN','MARY']
        len = len(AdmnNm)

        found = False

        for i in range(len):
            if Name == AdmnNm[i]:
                print("valid Admin", Name ,'found in', i+1, 'position')
                found = True
                break

        if found == False:
            print('Admin person not found')
else:
    print ("invalid group")


















