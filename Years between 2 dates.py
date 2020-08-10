import datetime

#x=datetime.date(input("Enter Date :"))
#dob = datetime.date(x)

dob = datetime.date(1980,7, 20)


def age():
       today = datetime.date.today()

       years = today.year - dob.year


       if today.month < dob.month or (today.month == dob.month and today.day < dob.day):

              years -= 1

       return years
       

def age2():

       today = datetime.date.today()

       this_year_birthday = datetime.date(today.year, dob.month, dob.day)


       if this_year_birthday < today:

              years = today.year - dob.year

       else:

              years = today.year - dob.year - 1

       return years

print(age())

print(age2())



