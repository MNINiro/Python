a = 50

def show():
    a = 10
    print("Local variable A",a) #it will access to local valiable a=10

    x = globals()['a']          #it will access to global valiable a=50
    print("Pulling global variable ",x)

    x = 40
    print("Value of X", x)      #here, we are modifying the value of x not global value a

show()
print("Global variable: A",a)
