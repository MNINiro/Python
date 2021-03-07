a = 0 #initialization
while a <= 10: # IT MUST BE TRUE
    print(a)
    a += 3         # a = a+1

#=====================================
computer_brands = ["Apple", "Asus", "Dell", "Samsung"]

i = 0
while i < len(computer_brands):    #4
   print(i,':',computer_brands[i])
   i = i + 1

#=====================================
print('Enter number to add to the sum. Enter 0 to stop')
s = 0
a = float(input('Enter Number : '))

while a != 0: #This condition must be true
     s += a
     # print('Current sum: ', s)
     a = float(input('Enter Number : '))

print('Total Sum = ', s)


