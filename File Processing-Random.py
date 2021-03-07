import pickle # this library is required to create b i nary f i les

class CarRecord:       # declaring a class without other methods
    def init (self) : # constructor
        self.VehicleID = ""
        self.Registration= ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00

ThisCar = CarRecord() # instantiates a car record

CarFile = open('Cars.DAT','rb+') # open file for binary read and write
Address = hash(ThisCar.VehicleID)
CarFileseek(Address)
pickle.dump(ThisCar,CarFile) # write a whole record to the b i nary file

CarFile.close () # close file

CarFile = open('Cars.DAT','rb' ) # open file for binary read
Address= hash(VehicleID)

CarFile. seek(Address)
ThisCar = pickle.load(CarFile) # load record from fi l e

CarFile . close()
