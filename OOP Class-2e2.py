# Property Decorators - Getters, Setters, and Deleters 
class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
       # self.email = first + '.' + last + '@outlook.com'

    @property
    def email(self):    # now email method is an attribute
        return '{}.{}@outlook.com'.format(self.first, self.last)
                      
    @property
    def fullname(self): # now fullname method is an attribute
        return '{} {}'.format(self.first, self.last)

    @fullname.setter            #Setter
    def fullname(self, name):
        first, middle, last = name.split(' ')
        self.first = first
        self.middle = middle
        self.last = last

emp_1 = Employee('John','Smith')
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
 
emp_1.fullname = 'Salman mia khan'  # it will show error messsage unless we need to use @fullname.setter decorators

print(emp_1.first)
print(emp_1.middle)
print(emp_1.last)
##print(emp_1.email) # it will show only memory address. to solve this problem
                    # we need to use @property method
# print(emp_1.email())
# print(emp_1.fullname()) # same @property methos can be used before fullname
print(emp_1.fullname)







