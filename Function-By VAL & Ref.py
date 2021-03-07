##Pass by reference vs value

##All parameters (arguments) in the Python language are passed by reference.
##It means if you change what a parameter refers to within a function,
##the change also reflects back in the calling function. For example 

### Function definition is here
# glst = [110, 220, 330] #global list
#
# def changeme(mylist):
#      "This changes a passed list into this function"
#      print("Actual global values in the list:", glst)
#      print("Actual local values in the list:", mylist)
#
#      Nlist=[11,12,13];
#      Nlist.extend([1, 2, 3, 4])
#      print("Values inside the function: ", Nlist)
#
#      Nlist.append(glst)
#      print('Nlist:',Nlist)
#
#      Nlist.append(mylist)
#      print('Nlist:',Nlist)
#      return
#
#  # Main body====== Now you can call changeme function
# mylist = [10, 20];
#
# changeme(mylist);
# print("")
# print("Values outside the function: ", glst)




# =============================================

##There is one more example where argument is being passed by reference
##and the reference is being overwritten inside the called function.

# Function definition is here
def changeme(mylist):
  "This changes a passed list into this function"
  mylist = [1,2,3,4]; # This would assign new reference in mylist
  print("Values inside the function: ", mylist)
  #return

# Now you can call changeme function
mylist = [10,20,30];
print( "Values outside the function: ", mylist)
changeme(mylist);

















