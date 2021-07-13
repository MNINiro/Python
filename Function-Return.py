#following example to show, how one function returns another function

def disp(st): #parameter passing #2
    print("Display function") #3
    return st #4 st = show()

def show():
    return 'Show function'

s_show = disp(show()) #1 first calling disp function, which will print "Display Function". Then it will return st means "show" in s_show
print(s_show)   #it will print 'Show function'


