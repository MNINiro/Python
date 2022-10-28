from datetime import date

# d1 = date(2000, 1, 1)
# d2 = date(2020, 11, 9)
#
# dt = d2 - d1
# print ('Number of days :', dt.days)



# Subtract from today's date

# import datetime
#
# today = datetime.date.today()
#
#
# dt = today - d1
# print (dt.days)


# Calculate number of months

from datetime import datetime

# def diff_month(d1, d2):
#     print('d1 year:',d1.year)
#     print('d1 month:',d1.month)
#     print('d2 year:',d2.year)
#     print('d2 month:',d2.month)
#     print('Number of years:', d1.year - d2.year)
#     print('Number of months:', d1.month - d2.month)
#
#     return (d1.year - d2.year) * 12 + d1.month - d2.month
#
# ##assert diff_month(datetime(2010,10,1), datetime(2010,9,1))
#
#
# date1 = date(2016, 5, 1)
# date2 = date(2018, 2, 23)
#
# print('Number of months:',diff_month(date2,date1))

# time difference

import datetime as dt
start_time = '10:33:30'
finish_time = '11:10:25'
ft = '%H:%M:%S'
td = datetime.strptime(finish_time, ft) - datetime.strptime(start_time, ft)
print(td)


