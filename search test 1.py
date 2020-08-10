import csv

def searchfile(filename):
    Id = []
    names = []
    emails = []
    month_joined = []
    status = []

    with open ("D:/Members.txt") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
         
        for line in csvReader:
         line = line.rstrip('\n')
         Id,names,emails,month_joined,status = line.split(',')
         
         Id.append(line[0])            
         print(Id)




##        for row in csvReader:
##            Id.append(row[0])
##            names.append(row[1])
##            emails.append(row[2])
##            month_joined.append(row[3])
##            status.append(row[4])
##
##    return Id, names, emails, month_joined, status



##while True:
##        query_ID = input('Enter Member id :')
##
##        for i in range(5):
##            if query_ID == ID[i]:
##                print('the name of',query_ID,'is',names[i],'email is',emails[i],'joined in',month_joined[i],'and status is',status[i])


##Id, names, emails, month_joined, status = searchfile("D:/Members.txt")


##for i in range(5):
##    print(i)
##    print(Id[i],',',names[i],',',emails[i],',',month_joined[i],',',status[i])
