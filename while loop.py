# a = 0 #initialization
#
# while a <= 10: # IT MUST BE TRUE
#     print (a)
#     a += 1         # a = a+1

##=====================================
#
# counter = 0
#
# while counter <= 10:
#     print (counter)
#     counter += 2


####=====================================

##computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
##print(len(computer_brands))
##print(len(computer_brands[0]))

####=====================================

# computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
#
# i = 0
# while i < len(computer_brands):
#    print(i,':',computer_brands[i])
#    i = i + 1

####=====================================

a = 1
s = 0

print('Enter number to add to the sum')
print('Enter 0 to stop')

while a != 0:
     print('Current sum: ', s)
     a = float(input('Enter Number : '))
##     a = float(a)
     s += a

print('Total Sum = ', s)


