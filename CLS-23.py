StudentName = []
StudentMark = []

ClassSize = int(input("Enter Class Size:"))
SubjectNo = int(input("Enter number of subjects:"))

i = 0
while i != ClassSize:
    StName = input("Enter Name:")
    StudentName.append(StName)

    Total = 0
    for sub in range(SubjectNo):
        Marks = int(input("Enter marks:"))
        Total += Marks

    StudentMark.append(Total)
    i += 1
print("Name", " ", "Total Marks", " ", "Average", " ", "Grade")
for count in range(ClassSize):
    Average = int(StudentMark[count] / SubjectNo)
    if Average >= 70:
        print(StudentName[count], " ", StudentMark[count], " ", Average, " ", "Distinction")
    elif Average >= 55:
        print(StudentName[count], " ", StudentMark[count], " ", Average, " ", "Merit")
    elif Average >= 40:
        print(StudentName[count], " ", StudentMark[count], " ", Average, " ", "Pass")
    else:
        print(StudentName[count], " ", StudentMark[count], " ", Average, " ", "Fail")
