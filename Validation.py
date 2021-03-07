##name = input("Enter Name :")
##
##while len(name) > 4:
##    print("Too long")
##    name = input("Enter Name :")
##
##if len(name) <= 4:
##    print("Perfect")


    
##status =  input("Enter membership active status 'T/F': ")
##status = status.upper()
##
##while ((status != 'TRUE') and (status != 'FALSE')):
##       print('Wront input')
##       status =  str(input('Please enter either True or False :'))
##       status = status.upper()
##      
##    
##if (status == 'TRUE') or (status == 'FALSE'):
##    print("Correct input")


from datetime import date 
##mj = datetime(2019, 3, 5)
##print(mj)
##Renewal_date = mj + timedelta(365)
##print (Renewal_date)

##t = datetime.datetime(2012, 2, 23, 0, 0)
t =  date.today()
dd= str(t.month)+ "-" + str(t.day) + "-" + str(t.year)
print(dd)
