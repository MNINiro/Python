# list
somelist = [1,2,4,5,7]

# to be honest not sure of a good way to do this

while True:
    if len(somelist) == 1:
	# will exit the loop once its found
	    print("Item Found: %i" % somelist[0])
	    break

    #somelist.remove(somelist[-1]) # last entry
    somelist.remove(somelist[0]) # first entry


# you should look at the math module. It may have what you need
 
# # in case I misread
# for n in somelist:
# 	if n != 2 or n !=4: # "!=" means not equal
# 		somelist.remove(n)
