#=== Ex-1 ===
def disp1():
    def show1():
        print("This is show function") #finally this result will be shown
    print("This is disp function") #this part will execute at the first
    show1() #now it will call nested disp function

#=== Ex-2 ===
def disp2():
    def show2():
        return 'Show2 function'
    result = show2() + 'Disp2 function' #show2() is getting result because of return function
    return result

#=== Ex-3 ===
def disp3(st): #parameter passing
    def show3():
        return 'Show3 function'
    result = show3() + st + 'Disp3 function'
    return result

#==== Main Body ====

disp1()
print(disp2())
print(disp3(' InCIS '))
