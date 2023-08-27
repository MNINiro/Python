# === Ex-1 ===
# class Mobile:
#
#     @classmethod
#     def showModel(cls):
#         print('iPhone')


# Mobile.showModel()  # Perfect way to use classmethod. calling class method

# === alternate way===
# x = Mobile            # creating instance then call (not the perfect way for classmethod
# x.showModel()         #we should use instance method instead of class method

# #=== Ex-2 === Following example is the right way to use classmethod
# class Mobile1:
#     fp = 'Yes'
#
#     @classmethod
#     def showModel(cls):
#         print('Finger Print:', cls.fp) #accessing to the class variable
#
# Mobile1.showModel()

# #=== Ex-3 === Following example is the right way to use classmethod
# class Mobile1:
#     fp = 'Yes'  # class variable
#
#     @classmethod
#     def showModel(cls, storage):
#         cls.storage = storage
#         print('Finger Print:', cls.fp)  # accessing to the class variable
#         print('Storage:', cls.storage)
#
#
# Mobile1.showModel('256GB')

# ====================
class Student:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Steve', 25)

    # def getobject(self):      # This method will show error
    #     return self('Steve', 25)


std = Student.getobject()
print(std.name)  # 'Steve'
print(std.age)  # 25