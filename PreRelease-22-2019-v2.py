#================== AppendRecord to file ===========================
from datetime import date 

def AppendRecord(ID,MName,email,month_joined,status,RDate):

    renewal_date = str(RDate.year)+ "-" + str(RDate.month) + "-" + str(RDate.day) # to convert date into string
    

    record = (ID+','+MName+','+email+','+month_joined+','+status+','+renewal_date)
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

#===================== Adding moreRecords into the file ========================
from datetime import datetime, timedelta

def addRecords():
        MemID = str(input("Enter Membership ID: "))

        while len(MemID) > 4:           # Validation. Length check
            print("Too long")
            MemID = str(input("Enter Membership ID: "))

        if len(MemID) <= 4:
            print("Perfect")

        MName =  str(input("Enter Name: "))
        email =  str(input("Enter email address: "))
        mj =  str(input("Enter month joined: "))

        x = datetime.strptime(mj,"%Y-%m-%d")
        RD = x + timedelta(365)
       
        

        status =  str(input("Enter membership active status 'True/False': ")) # Validation. Status can be either True or False
        status = status.upper()

        while ((status != 'TRUE') and (status != 'FALSE')):
               print('Wront input')
               status =  str(input('Please enter either True or False :'))
               status = status.upper()
           
        if (status == 'TRUE') or (status == 'FALSE'):
            print("Correct input")


        AppendRecord(MemID,MName,email,mj,status,RD)

        yn= input('Do you want to add more record?')
        yn.upper()
        if yn == 'Y':
            addRecords()
        else:
            exit


#===================== searchRecord ========================

import csv

def searchRecord(mID):
    with open('Members.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if row[0] == mID:
                print(f'\t Member ID: {row[0]} whos Name is {row[1]} and email address is {row[2]} has joined in {row[3]} and Membership status is {row[4]}.')
                break
 

#====================== defaulters ==========================
from datetime import datetime

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

               dflt = row[0]+'s membership has expired' #,row[1],row[2] to added
               
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
    menu['2']="Show all records"
    menu['3']="Search Record"
    menu['4']="Defaulters list"
    menu['5']="Exit"
        
    while True:
        options=menu.keys()

        for entry in options:
            print(entry, menu[entry])

        selection=input("Please Select:")
        if selection =='1':
            addRecords()
        elif selection == '2':
            AllRecords()
        elif selection == '3':
            mID = str(input('Enter Member ID :'))
            searchRecord(mID)
        elif selection == '4':
            defaulters()
        elif selection == '5':
            break
        else:
            print("Unknown Option Selected!")

     
       
MainMenu()
    


















