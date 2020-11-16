##x = 5
##
##for i in range(6):
##    z = i//x
##    print(z)
##    x -= 1
##    if x == 0:
##        break

NumberString = input ("enter an integer : ")

try:
    n = int(NumberString)
    print(n)
except:
    print(" This was not an integer" )
    
