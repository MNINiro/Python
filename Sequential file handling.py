import pickle # this library is requi red to create b inary f i les

class CarRecord:
    def __init__(self) :
        #declaring a class without other methods
        # constructor
        self .VehicleID = ""
        self.Registration= " "
        self.DateOfRegistration = None
        self.EngineSize = 0
        self .PurchasePrice = 0.00
        
ThisCar = CarRecord() # instantiates a car record
ThisCar.EngineSize = 2500

##ThisCar = CarRecord()
Car = [ThisCar for i in range(100)] # make a list of 100 car records
Car[1].EngineSize = 2500 # assigning value to a field of the 2nd car in list

Car = [ThisCar for i in range (100)]

CarFile = open ('Cars.DAT', 'wb' ) # open file for binary write

for i in range(100): # loop for each array element
    pickle.dump (Car[i], CarFile) # write a whole record to the binary file

CarFile.close() # close file


CarFile = open ('Cars.DAT','rb') # open file for binary read

Car= [] # start with empty list

while True: # check for end of file
    Car.append(pickle.load(CarFile) ) # append record from file to end of list

CarFile. close ()
