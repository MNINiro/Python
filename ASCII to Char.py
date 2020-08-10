# Program to find the ASCII value of the given character

# Uncomment to take character from user


ASC = input("Enter a character: ")
Encrypt = ord(ASC)
print(Encrypt)
print("The ASCII value of '" + ASC + "' is",ord(ASC))
x = Encrypt + 2
print(x)

y = chr(x)
print(y)


##
##for i in range(2000,5000):
##    print(i,' ',chr(i))
##    
    


##N = int(input("Enter a Number: "))
####x =(chr(N))
##
##print("The Ordinal value of '" + str(N) + "' is", (chr(N)))

##for i in range(255):
##    print(i,' :',chr(i))


