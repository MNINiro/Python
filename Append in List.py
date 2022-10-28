A = []
B = []

# First possibilty : using while loops
# you need to have a counter

X=5
i = 0
while (i < X):
   A.append(input('Enter value for X :'))
   # and increment it yourself
   i+=1

# you need to reset it
Y=5
i = 0
while (i < Y):
   B.append(input('Enter value for Y :'))
   # and increment it again
   i+=1



# No need to create a counter======================

##X=5
##for x in range(X):
##    A.append(input('Enter value for X :'))
##    # No need to increment the counter
##
### no need to reset the counter
##Y=5
##for x in range(Y):
##    B.append(input('Enter value for Y :'))

##================================================
X=5
Y=5
def repeat(limit):
    if hasattr(repeat,"counter"):
        repeat.counter += 1
        return repeat.counter < limit
    repeat.limit   = limit
    repeat.counters = 0
    return limit > 0 and True

while repeat(X):
    A.append(input('Enter value for X :'))

while repeat(Y):
    B.append(input('Enter value for Y :'))
