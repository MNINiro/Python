##class A:
##    def add(self, x, y):
##        print(x + y)
##
##class B:
##    def call_a(self):
##        A.add(self, 1, 2)
##
##b = B()
##b.call_a()

#============================

class Test1(object): # always inherit from object in 2.x. it's called new-style classes. look it up

    def method1(self, a, b):
        return a + b

    @staticmethod
    def method2(a, b):
        return a - b

    @classmethod
    def method3(cls, a, b):
        return cls.method2(a, b)

t = Test1()  # same as doing it in another class

Test1.method1(t, 1, 2) #form one of calling a method on an instance
print(t.method1(1, 2))        # form two (the common one) essentially reduces to form one

Test1.method2(1, 2)  #the static method can be called with just arguments
print(t.method2(1, 2))      # on an instance or the class

Test1.method3(1, 2)  # ditto for the class method. It will have access to the class
print(t.method3(1, 2))
