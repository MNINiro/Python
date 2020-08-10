# Functions  'WriteRecord' and 'addRecord' have been written only for tutorial purposes.
# These two functions are not required to add records in the members.text file
# Function 'AppendRecord' and 'moreRecords' are sufficient for this program


#================== WriteRecord to file ===========================

def WriteRecord(ID,MName,email,month_joined,status):

    record = (ID+','+MName+','+email+','+month_joined+','+status)
    FileHandle = open("Members.txt", "w")
    FileHandle.write(record)
    FileHandle.write('\n')
    FileHandle.close()
    return

#================== AppendRecord to file ===========================

def AppendRecord(ID,MName,email,month_joined,status):

    record = (ID+','+MName+','+email+','+month_joined+','+status)
    FileHandle = open("Members.txt", "a")
    FileHandle.write(record)
    FileHandle.write('\n')
    FileHandle.close()
    return

#================== Show AllRecord ===========================

def AllRecords():

    FileHandle = open("Members.txt", "r")
    Text = FileHandle.read()
    print(Text)
    
    while len(Text)>0:
        Text = FileHandle.readline()
        print(Text)
    FileHandle.close()
    return

#================== addRecord to write in the file ===========================
            
def addRecord():
    MemID = str(input("Enter Membership ID: "))

    while len(MemID) > 4:           # Validation. Length check
            print("Too long")
            MemID = str(input("Enter Membership ID: "))

    if len(MemID) <= 4:
            print("Perfect")
            
    email =  str(input("Enter email address: "))
    mj =  str(input("Enter month joined 'yyyy/mm/dd': "))

    status =  str(input("Enter membership active status 'True/False': ")) # Validation. Status can be either True or False
    status = status.upper()

    while ((status != 'TRUE') and (status != 'FALSE')):
           print('Wront input')
           status =  str(input('Please enter either True or False :'))
           status = status.upper()
       
    if (status == 'TRUE') or (status == 'FALSE'):
        print("Correct input")

    WriteRecord(MemID,MName,email,mj,status)

#===================== Adding moreRecords into the file ========================
    
def moreRecords():
        MemID = str(input("Enter Membership ID: "))

        while len(MemID) > 4:           # Validation. Length check
            print("Too long")
            MemID = str(input("Enter Membership ID: "))

        if len(MemID) <= 4:
            print("Perfect")

        MName =  str(input("Enter Name: "))
        email =  str(input("Enter email address: "))
        mj =  str(input("Enter month joined: "))

        status =  str(input("Enter membership active status 'True/False': ")) # Validation. Status can be either True or False
        status = status.upper()

        while ((status != 'TRUE') and (status != 'FALSE')):
               print('Wront input')
               status =  str(input('Please enter either True or False :'))
               status = status.upper()
           
        if (status == 'TRUE') or (status == 'FALSE'):
            print("Correct input")

        AppendRecord(MemID,MName,email,mj,status)

        yn= input('Do you want to add more record?')
        yn.upper()
        if yn == 'Y':
            moreRecords()
        else:
            exit

#===================== searchRecord ========================
        
from datetime import datetime
import csv

def searchRecord(mID):
    with open('Members.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if row[0] == mID:
                print(f'\t Member ID: {row[0]} whos Name is {row[1]} and email address is {row[2]} has joined in {row[3]} and Membership status is {row[4]}.')
                break
 

#====================== defaulters ==========================
        
def defaulters():
    open('defaulters.txt', 'w').close()         # to remove existing data from the defaulters.txt file
    
    with open('Members.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:                    # strftime() is used to convert a time to string. The ‘time’
                                                                 # must be of a type struct_time which is a ‘tuple’ or list/array of time components.
                                                                 # (A ‘tuple’ is a unique python structure). strptime is used to
                                                                 #convert a date string to a datetime object.
           
           mj = datetime.strptime(row[3], '%Y-%m-%d')
           cday = datetime.today().strftime("%Y-%m-%d")
           cday = datetime.strptime(cday,"%Y-%m-%d")
           
           NoOfDays = cday - mj
           if NoOfDays.days > 365:
               print(row[0],"'s membership has expired")

               dflt = row[0]+'s membership has expired'
               
               FileHandle = open("defaulters.txt", "a")
               FileHandle.write(dflt)
               FileHandle.write('\n')
               FileHandle.close()
        print('Defaulters list has been saved in defaulters.txt file')
        
    
 #====================== MainMenu ==========================       

def MainMenu():
    print()
    menu = {}
    menu['1']="Add Record."
    menu['2']="Append Records."
    menu['3']="Show all records"
    menu['4']="Search Record"
    menu['5']="Defaulters list"
    menu['6']="Exit"
        
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
            AllRecords()
        elif selection == '4':
            mID = str(input('Enter Member ID :'))
            searchRecord(mID)
        elif selection == '5':
            defaulters()
        elif selection == '6':
            break
        else:
            print("Unknown Option Selected!")

     
       
MainMenu()
    


















