# n = int(input("Enter Number :"))
#
# if n < 0:
#       print("Absolute value of ",n," is", -n)
# else:
#       print("The absolute value of ",n," is", n)
      
#Example

ban = 80
eng = 80
CSE = 80

total = int(ban) + int(eng) + int(CSE)
print('Total :', total)

average = total/3
print('Average :',average)

if average >= 80:
      print("A Grade")
elif average >= 70:
            print("B Grade")
elif average >= 60:
            print("C Grade")
else:
      print('Fail')

