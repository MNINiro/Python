
class A:
    def add(self, x, y):
        print(x + y)

class B:
    def call_a(self):
        A.add(self, 1, 2)

b = B()
b.call_a()

#=======================================

class Test1(object): # always inherit from object in 2.x. it's called new-style classes. look it up

    def method1(self, a, b):
        return a + b

    @staticmethod
    def method2(a, b):
        return a + b

    @classmethod
    def method3(cls, a, b):
        return cls.method2(a, b)

t = Test1()  # same as doing it in another class

Test1.method1(t, 1, 2) #form one of calling a method on an instance
print(t.method1(1, 2))        # form two (the common one) essentially reduces to form one

Test1.method2(1, 2)  #the static method can be called with just arguments
print(t.method2(1, 2))      # on an instance or the class

Test1.method3(1, 2)  # ditto for the class method. It will have access to the class
print(t.method3(1, 2))      # that it's called on (the subclass if called on a subclass) 
                     # but will not have access to the instance it's called on 
                     # (if it is called on an instance)

#=======================================




class CurrentValue:

    def __init__(self, value):
        self.value = value

    def set_val(self, k):
        self.value = k

    def get_val(self):
        return self.value


class AddValue:

    def av(self, ocv):
        print('Before:', ocv.get_val())

        num = int(input('Enter number to add : '))
        nnum = num + ocv.get_val()
        ocv.set_val(nnum)
        print('After add :', ocv.get_val())


cvo = CurrentValue(5)

avo = AddValue()

avo.av(cvo)
