#===Examle-1====
# import calendar
#
# # print(calendar.month(2021, 10))
# cal = calendar.month(2021, 10)
# print("Here is the calendar:")
# print(cal)

# #===Examle-2====
# import time
#
# localtime = time.asctime(time.localtime(time.time()))
# print ("Local current time :", localtime)

#===Examle-3====
# from time import time, ctime
# epoch = time()      #Seconds
# print(epoch)
#
# ct = ctime(epoch)   #Seconds to current time
# print(ct)
#
# print(ctime())      #Current time

#===Examle-4====
# from time import time, ctime, localtime
#
# stobj = localtime()
# print(stobj)
# print(stobj.tm_mday)
# print(stobj.tm_year)
# print(stobj.tm_mon)
# print(stobj.tm_hour)
# print(stobj.tm_min)
# print(stobj.tm_sec)

# ===Examle-5====
from datetime import datetime
# dt1 = datetime(year=2021, month=1, day=20)
# dt2 = datetime(month=3, year=2020, day=24)
# dt3 = datetime(2014, 5, 5)
# dt4 = datetime(2016, 5, 5,10,30)
# print(dt1)
# print(dt2)
# print(dt3)
# print(dt4)
#============================
# dtY = int(input('Enter Year:'))
# dtM = int(input('Enter Month:'))
# dtD = int(input('Enter Day:'))
# ddate = datetime(dtY,dtM,dtD)
# print(ddate)
#
# print(ddate.year)
# print(dt1.month)
# print(dt1.day)

# ct=datetime.now()
# print(ct)
# print(ct.year)

# ===Examle-6====
from datetime import time
t1 = time(hour=20, minute=1, second=20)
t2 = time(11, 15, 55)
print(t1.hour)
print(t1.minute)
print(t1.second)
print(t2)