from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod # it's an inteface. Known as Abstract method
    def disp1(self):
        pass

    @abstractmethod  # it's an inteface. Known as Abstract method
    def disp2(self):
        pass

#without defining abstractmethods, we can't create object of any interface.
#So, we are creating following subclasses with methods to create required objects
class Child(Father):
    def disp1(self): # disp1 abstract method has been inherited and object can be created but not for disp2(also inherited).
        print("Child Class")
        print("Disp1 Abstract method")

class GrandChild(Child):
    def disp2(self): #here, disp2 properly inherited through child class from Father class
        print("GrandChild Class")
        print("Disp2 Abstract method")

gc = GrandChild()
gc.disp1()
gc.disp2()
