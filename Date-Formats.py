from datetime import datetime
dt = datetime.today()
print(dt)
print(type(dt))
print()

newd1 = dt.strftime("%B %d, %Y")
print(newd1)
print()

newd1 = dt.strftime("%d/%b/%Y")
print(newd1)
print()

newd1 = dt.strftime("%d-%m-%Y")
print(newd1)
print()

newd1 = dt.strftime("%H, %M, %S") #24-hour format
print(newd1)
print()

newd1 = dt.strftime("%I, %M, %S") #12-hour format
print(newd1)
print()