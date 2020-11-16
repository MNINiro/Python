import datetime
import time


# Using date.today()

todaysDate = datetime.date.today();
print("Today's date - Using date class:%s"%todaysDate);

 

# Using date.fromtimestamp()

todaysDate = datetime.date.fromtimestamp(time.time());
print("Today's date - Using time class:%s"%todaysDate);



