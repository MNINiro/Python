student_ID = ['5', '9', '3', '7', '10', '45', '25']
student_Name = ['Ali', 'Ahmed', 'Badrul', 'Muddasir', 'Alvi', 'Nahiyan', 'Fahmid']
section = ['red', 'blue', 'green', 'red', 'blue', 'green', 'yellow']

search_Item = input('Enter Student ID:')

ln = len(student_ID)
found = False
i = 0

# for i in range(ln):
#     if search_Item == student_ID[i]:
#         found = True
#         break

while i <= ln-1:
    if search_Item == student_ID[i]:
        found = True
        break
    i += 1

if not found:
    print('ID does not exits')
else:
    print('Student ID found in position', i+1)
    print('Student Name is', student_Name[i])
    print('Section is', section[i])
