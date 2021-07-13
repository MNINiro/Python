##Pass by reference vs value

##All parameters (arguments) in the Python language are passed by reference.
##It means if you change what a parameter refers to within a function,
##the change also reflects back in the calling function. For example 

### Function definition is here

def changeme(mylist):
     "This changes a passed list into this function"
     print("Actual values in the list:", mylist)

     mylist=[10,20,30]; #replaced
     mylist.append([50,60,70]);
     mylist.append([1, 2, 3, 4]);
     mylist.append([5,6,7]);
     mylist.append([1, 2, 3, 4]);
     print(mylist)
     print("")
     print("Popped :",mylist.pop())
     print("After Popped :", mylist)
     print("")
##     del mylist[1:3]
     del mylist[:]
     print("Values inside the function: ", mylist)
     return
# Now you can call changeme function
mylist = [11, 22, 33];
changeme(mylist);
print("Values outside the function: ", mylist)


