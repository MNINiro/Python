#Ahnaf:
#
# stud = []
# sub = []
# i = 1
# total = 0
# a = 0
# b = 1
#
# while i <= 2:
#     x = int(input("Enter Student ID:"))
#     stud.append(x)
#     i += 1
#
#     j = 1
#     while j <= 2:
#         y = float(input("Subject marks:"))
#         sub.append(y)
#         j += 1
#     print(sub)
#
#     total = sub[a] + sub[b]
#     print(f"total marks of two subjects:{total}")
#     a += 2
#     b += 2

#Sumehra
student = []
subject = []

i = 0
a = 0
b = 1
total = 0

while (i <= 2):
    studentID = input("Please enter your ID number: ")
    student.append(studentID)
    print(student)

    i = i + 1

    j = 0
    while (j <= 1):
        subjMarks = int(input("Please enter the mark you obtained in the subject: "))
        subject.append(subjMarks)
        print(subject)
        j = j + 1

    total = subject[a] + subject[b]
    print("The total mark that you received from the two subjects is", total)
    a = a + 2
    b = b + 2
    total = 0
