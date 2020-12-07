# #===Ex-2===
# # Python program to demonstrate protected members
#
# # Creating a base class
# class Base:
#     def __init__(self):
#         # Protected member
#         self._a = 2
#
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         # Calling constructor of Base class
#         Base.__init__(self)
#         print("Calling protected member of base class: ")
#         print(self._a)
#
#
# obj1 = Derived()
# obj2 = Base()
#
# # Calling protected member outside class will  result in AttributeError
# print(obj2.a)

#===Ex-2===
# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforAGeeks"
        self.__c = "Geeksfor__CGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
# obj1 = Base()
# print(obj1.a)
# print(obj1.__c) #will raise an AtrributeError

# obj3 = Derived()
# print(obj3.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
