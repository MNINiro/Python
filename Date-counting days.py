import datetime
import time
##
##from datetime import date
##
##today = date.today()
##
####datetime.date(2007, 12, 5)
####today == date.fromtimestamp(time.time())
##print(today)
##
##my_birthday = date(today.year, 6, 24)
##if my_birthday < today:
##       my_birthday = my_birthday.replace(year=today.year + 1)
##
##print(my_birthday)
####print(datetime.date(2008, 6, 24))
##time_to_birthday = abs(my_birthday - today)
##print(time_to_birthday.days)

#==============================================================

from datetime import datetime
## 
##date_time_str1 = 'Jun 28 2018  7:40AM'
##date_time_str2 = 'September 18, 2017, 22:19:55'
##date_time_str3 = 'Sun,05/12/99,12:30PM'
##date_time_str4 = '2018-03-12T10:12:45Z'
## 
##date_time_obj1 = datetime.strptime(date_time_str1, '%b %d %Y %I:%M%p')
##date_time_obj2 = datetime.strptime(date_time_str2, '%B %d, %Y, %H:%M:%S')
##date_time_obj3 = datetime.strptime(date_time_str3, '%a,%d/%m/%y,%I:%M%p')
##date_time_obj4 = datetime.strptime(date_time_str4, '%Y-%m-%dT%H:%M:%SZ')
## 
##print('For Time1   Date:',date_time_obj1.date(), 'Time:', date_time_obj1.time())
##print('For Time2   Date:',date_time_obj2.date(), 'Time:', date_time_obj2.time() )
##print('For Time3   Date:',date_time_obj3.date(), 'Time:', date_time_obj3.time() )
##print('For Time4   Date:',date_time_obj4.date(), 'Time:', date_time_obj4.time() )

#==============================================================

##from datetime import date
##f_date = date(2014, 7, 2)
##l_date = date(2014, 7, 11)
##delta = l_date - f_date
##print(delta.days)

#==============================================================

dt = datetime(2018, 1, 1)
milliseconds = int(round(dt.timestamp() * 1000))
print(milliseconds)


