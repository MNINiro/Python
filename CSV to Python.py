##The quotechar optional parameter tells the writer which character to use
##to quote fields when writing. Whether quoting is used or not, however,
##is determined by the quoting optional parameter:
##
##If quoting is set to csv.QUOTE_MINIMAL, then .writerow() will quote fields
##only if they contain the delimiter or the quotechar. This is the default case.

##If quoting is set to csv.QUOTE_ALL, then .writerow() will quote all fields.

##If quoting is set to csv.QUOTE_NONNUMERIC, then .writerow() will quote all fields
##containing text data and convert all numeric fields to the float data type.

##If quoting is set to csv.QUOTE_NONE, then .writerow() will escape delimiters
##instead of quoting them. In this case, you also must provide a value for the
##escapechar optional parameter.

#====================== Writing records in a csv file =======================

##import csv
##
##with open('employee_file.csv', mode='w') as employee_file:
##    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
##
##    employee_writer.writerow(['name','department','birthday month'])
##    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
##    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
##
##
##
##
###==================================
###alternate method:
##
##with open('employee_file.csv', mode='w') as csv_file:
##    fieldnames = ['emp_name', 'dept', 'birth_month']
##    
##    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
##
##    writer.writeheader()
##    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
##    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

#==================================

##with open('employee_birthday.txt') as csv_file:
##
##    
####with open('employee_file.csv') as csv_file:
##    csv_reader = csv.reader(csv_file, delimiter=',')
##    line_count = 0
##    
##    for row in csv_reader:
##        if line_count == 0:
##            print(f'Column names are: {", ".join(row)}')
##            line_count += 1            
##        else:
##            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
##            line_count += 1
##            
##
##    print(f'Processed {line_count} lines.')




import csv

def readMyFile(filename):
    dates = []
    scores = []

    with open("testCSV.csv") as csvDataFile:
        csvReader = csv.reader(csvDataFile)

        for row in csvReader:
            dates.append(row[0])
            print(dates)
            scores.append(row[1])
            print(scores)

    return dates, scores


dates,scores = readMyFile('file.csv')

for i in range(4):
    print(dates[i],'|',(scores[i]))



