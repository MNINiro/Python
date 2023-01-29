classSize = 3
subjects = 2
sID = []
sTot = []

for student in range(classSize):
    id = input("Enter Student's id:")
    sID.append(id)

    Total = 0
    for marks in range(subjects):
        mrk = float(input("Enter Subject Marks:"))
        while mrk < 0 or mrk > 100:
            print("Invalid. Please input again.")
            mrk = float(input("Enter Subject Marks:"))
        Total += mrk
    sTot.append(Total)

print("ID\t", "Marks")
for i in range(classSize):
    print(sID[i],':',sTot[i])