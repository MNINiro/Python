StudentName=[]
Subject=[]

for x in range(3):
    print()
    StNm = input('Enter Student Name :')
    StudentName.append(StNm)

    for y in range(2):
        Sub = int(input('Enter Subject Marks :'))
        Subject.append(Sub)

# print(StudentName, ' ',Subject)


a = 0
i = 2


for x in range(3):
    print("Student name is ",StudentName[x])

    total = 0

    for y in range(a, i):
        print("Subject marks :",Subject[y])
        total += Subject[y]

    print("Total :",total)

    a += 2
    i += 2

