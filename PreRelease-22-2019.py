def WriteRecord(ID,MName,email,month_joined,status):

    record = (ID+','+MName+','+email+','+month_joined+','+status)
    FileHandle = open("D:/Members.txt", "w")
    FileHandle.write(record)
    FileHandle.write('\n')

    FileHandle.close()
    return

def AppendRecord(ID,MName,email,month_joined,status):

    record = (ID+','+MName+','+email+','+month_joined+','+status)
    FileHandle = open("D:/Members.txt", "a")
    FileHandle.write(record)
    FileHandle.write('\n')
    FileHandle.close()
    return

def MultiLineRead():

    FileHandle = open("D:/Members.txt", "r")
    Text = FileHandle.read()
    print(Text)
    
    while len(Text)>0:
        Text = FileHandle.readline()
        print(Text)
    FileHandle.close()
    return

            
def addRecord():
    MemID = str(input("Enter Membership ID: "))
    MName =  str(input("Enter Name: "))
    email =  str(input("Enter email address: "))
    mj =  str(input("Enter month joined: "))
    status =  str(input("Enter membership active status: "))

    WriteRecord(MemID,MName,email,mj,status)

def moreRecords():
    for i in range(2):
        MemID = str(input("Enter Membership ID: "))
        MName =  str(input("Enter Name: "))
        email =  str(input("Enter email address: "))
        mj =  str(input("Enter month joined: "))
        status =  str(input("Enter membership active status: "))

        AppendRecord(MemID,MName,email,mj,status)


def read_from_file():
    with open("D:/Members.txt") as file:
         i=0
         for line in file:
            line = line.rstrip('\n')
            ID,Name,email,Month_joined,Status = line.split(',')

            sports_club[i] = ID
            i+=1
            sports_club[i] = Name
            i+=1
            sports_club[i] = email
            i+=1
            sports_club[i] = Month_joined
            i+=1
            sports_club[i] = Status
            i+=1

sports_club = {}
##print(sports_club)
read_from_file()
##print(sports_club)
    
  
def searchRecord():

##    found = False

    while True:
        query_ID = input('Enter Member id :')
   
        for x in range(0,len(sports_club),5):
            if query_ID in sports_club[x]:
                name = sports_club[x+1]
                email = sports_club[x+2]
                Month_joined = sports_club[x+3]
                Status = sports_club[x+4]
                print('the name of',query_ID,'is',name,'.','email address is',email,'.','joined in',Month_joined,'and status is',Status)
##                found = True
##                break
##        if query_ID == found:
##            print('Record not found')


def MainMenu():
    menu = {}
    menu['1']="Add Record."
    menu['2']="Append Records."
    menu['3']="Show all records"
    menu['4']="Search Record"
    menu['5']="Exit"
        
    while True:
        options=menu.keys()

        for entry in options:
            print(entry, menu[entry])

        selection=input("Please Select:")
        if selection =='1':
            addRecord()            
        elif selection == '2':
            moreRecords()
        elif selection == '3':
            MultiLineRead()
        elif selection == '4':
            searchRecord()
        elif selection == '5':
            break
        else:
            print("Unknown Option Selected!")

     
       
MainMenu()
    
##addRecord()
##moreRecords()
##MultiLineRead()        
##read_from_file()    
##searchRecord()

















