import calendar

cal = calendar.month(2005, 9)

print ("Here is the calendar:")
print (cal)


import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

print()

localtime = time.asctime(time.localtime(time.time()) )
print ("Local current time :", localtime)


