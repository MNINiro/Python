class nameset:
    def __init__(self, name, staffno):
        self.__name = name
        self.__staffno = staffno

    def setName(self, n):
        self.__name = n
        print(self.__name)

    def getHoursWorked(self,hw):
        self.__hoursWorked = hw
        return(self.__hoursWorked)


nm = nameset('MNI', 101)
nm.setName('Ahmed')
h = nm.getHoursWorked(72)
print(h)