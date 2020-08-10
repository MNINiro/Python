from datetime import date

d1 = date(2000, 1, 4)
d2 = date(2018, 2, 23)

dt = d2 - d1
print (dt.days)



### Subtract from today's date
##
##import datetime
##
##today = datetime.date.today()
##
##
##dt = today - d1
##print (dt.days)


# Calculate number of months

from datetime import datetime

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

##assert diff_month(datetime(2010,10,1), datetime(2010,9,1))


dt1 = date(2016, 5, 1)
dt2 = date(2018, 2, 23)

print(diff_month(dt2,dt1))
