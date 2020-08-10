import pickle # this library is requi red to create b inary f i les
ThisCar = CarRecord()
Car = [ThisCar for i in range (100)]

CarFile = open ('Cars.DAT', 'wb ' ) # open file for binary write
for i in range (lOO ) : # loop for each array eleme nt
        pickle.dump (Car[i], CarFile) # write a whole record to the b i nary file

CarFile.close() # close file

CarFile = open ('Cars.DAT','rb') # open file for binary read

Car= [] # start with empty list
while True: # check for end of file
    Car.append(pickle.load(CarFile) ) # append record from file to end of l i st

CarFile. close ()
