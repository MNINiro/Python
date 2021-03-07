import sys
print("Default: ",sys.getrecursionlimit())
sys.setrecursionlimit(2000) #we have changed default recursion limit to 2000 from 1000
print("Modified: ",sys.getrecursionlimit())

i = 0
def myFunc():
    global i
    i+=1
    print("InCIS",i)
    myFunc() #it will call 1000 time by default then show error.

myFunc()