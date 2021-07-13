import datetime as dt
import time

# Using date.today()
todaysDate = dt.date.today();
print("Today's date - Using date class:%s"%todaysDate);

# Using date.fromtimestamp()
todaysDate = dt.date.fromtimestamp(time.time());
print("Today's date - Using time class:%s"%todaysDate);



