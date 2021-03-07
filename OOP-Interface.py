from abc import ABC, abstractmethod

class Father(ABC): #Now, it is an Abstract class since it has both Abstract method and Concrete method
    @abstractmethod # it's an inteface. Known as Abstract method
    def disp(self):
        pass

    def show(self): #This method was written later
        print("Concrete Method")

# my = Father() #it will show error since, we can't create an object of an interface.

# class Child(Father):
#     pass
# c = Child() #it will also show error since, we can't create an object of an interface and Child has been inherited from Father class.

class Child(Father):
    def disp(self):
        print("Child class")
        print("Defining Abstract method")
c = Child()
c.disp()
