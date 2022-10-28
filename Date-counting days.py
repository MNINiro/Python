import datetime
from datetime import date

# today = date.today()
# print("today:",today)
# #
# my_birthday = date(today.year, 1, 1)
# print(my_birthday)
#
# if my_birthday < today:
#     my_birthday = my_birthday.replace(year = today.year + 1)
#     print("my birthday:",my_birthday)
#
# days_to_birthday = abs(my_birthday - today)
# print("Days to next birthday:",days_to_birthday.days)
# print()
# print(datetime.date(2008, 10, 24))
# #==============================================================
# from datetime import date
# dob = date(1972,8,29)
# today = date.today()
# age = (today.year - dob.year)-((today.month, today.day) < (dob.month, dob.day))
# print("Current age is",age)
# print()

# #==============================================================
# from datetime import datetime
#
# now = datetime.now() # current date and time
# year = now.strftime("%Y")
# # year = now.year
# print("year:", year)
#
# month = now.strftime("%m")
# print("month:", month)
#
# day = now.strftime("%d")
# print("day:", day)
#
# time = now.strftime("%H:%M:%S")
# print("time:", time)
#
# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)
# print()

#==============================================================
# from datetime import datetime
#
# timestamp = 502525555
#
# date_time = datetime.fromtimestamp(timestamp)
# print("Date time object:", date_time)
#
# d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
# print("Output 2:", d)
#
# d = date_time.strftime("%d %b, %Y")
# print("Output 3:", d)
#
# d = date_time.strftime("%d %B, %Y")
# print("Output 4:", d)
#
# d = date_time.strftime("%I%p")
# print("Output 5:", d)
# print()
#==============================================================
# from datetime import datetime
#
# date_time_str1 = 'Jun 28 2018  7:40AM'
# date_time_obj1 = datetime.strptime(date_time_str1, '%b %d %Y %I:%M%p')
# print('For Time1   Date:',date_time_obj1.date(), 'Time:', date_time_obj1.time())
#
# date_time_str2 = 'September 18, 2017, 22:19:55'
# date_time_obj2 = datetime.strptime(date_time_str2, '%B %d, %Y, %H:%M:%S')
# print('For Time2   Date:',date_time_obj2.date(), 'Time:', date_time_obj2.time())
#
# date_time_str3 = 'Sun,05/12/99,12:30PM'
# date_time_obj3 = datetime.strptime(date_time_str3, '%a,%d/%m/%y,%I:%M%p')
# print('For Time3   Date:',date_time_obj3.date(), 'Time:', date_time_obj3.time())
#
# date_time_str4 = '2018-03-12T10:12:45Z'
# date_time_obj4 = datetime.strptime(date_time_str4, '%Y-%m-%dT%H:%M:%SZ')
# print('For Time4   Date:',date_time_obj4.date(), 'Time:', date_time_obj4.time())
# print()
#==============================================================
from datetime import date

f_date = date(2014, 5, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print("delta:",delta.days)
print()
# #==============================================================
# dt = datetime(2018, 1, 1)
# milliseconds = int(round(dt.timestamp() * 1000))
# print(milliseconds)


