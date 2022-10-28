# n = int(input("Enter Number :"))
# # print(abs(n))
# if n < 0:
#       print("Absolute value of ",n," is", abs(n))
# else:
#       print("The absolute value of ",n," is", abs(n))
#
# Example

ban = input('Enter Bangla marks: ')
eng = input('Enter English marks: ')
CSE = input('Enter CSE marks: ')

# if (ban < 0) or (ban > 100):
#     print('Invalid Bangla marks')
#
# if (eng < 0) or (eng > 100):
#     print('Invalid Engling marks')
#
# if (CSE < 0) or (CSE > 100):
#     print('Invalid CSE marks')

total = int(ban) + int(eng) + int(CSE)
# print('Total :', total)

average = total / 3
# print('Average :', average)

if average >= 80:
    print("A Grade and the average is", average, 'Total is', total)

elif average >= 70:
    print("B Grade")
    print("Average is:", average)
    print('Total is:', total)
elif average >= 60:
    print("C Grade and the average is", average)
else:
    print('Fail')
