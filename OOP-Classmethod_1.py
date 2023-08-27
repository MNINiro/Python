# A class method decorator is a function that modifies a method of a class and
# expects the first argument to be the class object.It can be used to declare
# a method that can be called using the class name or an instance of the class.
# It can also be used to create factory methods that return objects of the class.

# One way to create a class method decorator is to use the @ classmethod built-in decorator.
# This decorator takes a function and returns a class method object.
# The first parameter of the function must be cls, which represents the class object.For example:


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_full_name(cls, full_name):
        first_name, last_name = full_name.split()
        return cls(first_name + " " + last_name)


# p = Person("Abrar Ahmed")

p = Person.from_full_name("John Smith")
print(p.name)  # John Smith

# In this example, the from_full_name method is decorated with @ classmethod,
# which makes it a class method.It takes a full name as an argument and returns
# a Person object with that name.The cls parameter is used to call the init method of the class.

# Another example:

'''
class Student:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Steve', 25)

    # def getobject(self):      	# This method will show error
    #     return self('Steve', 25)


std = Student.getobject()
print(std.name)  # 'Steve'
print(std.age)  # 25

'''
