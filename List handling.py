# Linear search

StudentID = [12, 20, 1, 55, 70]

search = int(input('Enter ID:'))

found = False

for i in range(len(StudentID)):
    if search == StudentID[i]:
        found = True
        print(StudentID[i], 'Found')

if not found:
    print('ID not found')


