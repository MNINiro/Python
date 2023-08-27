# '''
for id in range(3):
    stID = input('Enter Student ID:')

    total = 0
    for subjects in range(4):
        marks = int(input('Enter Marks:'))
        total = total + marks
    print(total)
# '''












'''
StudentID = []
TotalMarks = []

id = 0
while id < 3:
    stID = input('Enter Student ID:')
    StudentID.append(stID)

    total = 0
    subjects = 0
    while subjects < 4:
        marks = int(input('Enter Marks:'))
        total = total + marks
        subjects += 1

    TotalMarks.append(total)
    print(total)
    print()
    id += 1

print(StudentID)
print(TotalMarks)

for i in range(len(StudentID)):
    print('Student ID:', StudentID[i], 'received total:', TotalMarks[i])

'''
'''
for id in range(3):
    stID = input('Enter Student ID:')

    total = 0
    subjects = 0
    while subjects < 4:
        marks = int(input('Enter Marks:'))
        total = total + marks
        subjects = subjects + 1
    print(total)
    print()
    id = id + 1
'''
