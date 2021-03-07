class Person:

       # “Self” in Python works as a variable of function but it won’t invoke data.
       # In Python, functions in class access data via “self”
       # self is a default variable that contains the memory location of the current object.

       
       def __init__(self,name):
              self.name = name
              
              print(self.name)
              print(name)

       def PrintName(self):
              print(self.name)
              

p = Person("Niro")

print(p.name)

p.PrintName()

