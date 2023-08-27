SubjectMarks = []
total = 0

for counter in range(3):  # count-controlled loop
    marks = int(input('Enter subject marks:'))
    if marks >= 0 and marks <= 100:  # 0 <= marks <= 100:
        SubjectMarks.append(marks)
        total = total + marks
    else:
        print('Invalid marks entered')

print('Total:', total)
print('marks are:', SubjectMarks)

if len(SubjectMarks) == 0:
    print('Division is not possible')
else:
    avg = total / len(SubjectMarks)
    print("average marks is:", avg)
    print('Formatted output:', "{:.2f}".format(avg))
    print("Average marks:", f"{avg:.2f}")
