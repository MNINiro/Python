# Example-1
class shape:
    def __init__(self):
        self.__areaValue = 0
        self.__perimeterValue = 0

    def __del__(self):
        print("Shape deleted")

    def area(self):
        print("Area ", self.__areaValue)

    def perimeter(self):
        print("Perimeter ", self.__areaValue)


myCircle = shape()
del myCircle


# =========== Example-2 ===========

class Employee:

    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')


EmpObj = Employee()
del EmpObj
