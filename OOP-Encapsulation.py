# #===Ex-1===
# Python program to demonstrate protected members
# """
# Creating a base class
class Base:
    def __init__(self):
        # Protected member
        self._a = 2

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling protected member of base class: ")

obj1 = Derived()
obj2 = Base()

print(obj1._a)

# Calling protected member outside class will  result in AttributeError
print(obj2._a)
# """

#===Ex-2===
# Python program to
# demonstrate private members

# Creating a Base class
# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "Geeksfor__CGeeks"
#
#     def testProtected(self):
#         self.d = "Hello"
#         self.e = self.d + " " + self.__c
#         print(self.e)
#
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         # print(self.__c) //Will show error
#         # print(self.e)   //Will show error
#
# class child(Base):
#     def __init__(self,text):
#         self.__c = text #__c is not same as Base class __c
#         print(self.__c)
#         #super().__init__()

# Driver code
# obj1 = Base()
# print(obj1.a)
# print(obj1.__c) #will raise an AtrributeError

# obj3 = Derived()
# print(obj3.e)

# obj1.testProtected()

# ch = child("Hi")

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
