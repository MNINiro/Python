from datetime import timedelta, date
dy = int(input('Enter number of days to be added:'))
td = timedelta(days=dy) #after dy days
d = date.today()
print("Today",d)
print(f"After {dy} days:",d+td)

