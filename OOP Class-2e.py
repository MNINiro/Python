# Property Decorators - Getters, Setters, and Deleters 

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@outlook.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
 
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

emp_1.first = 'Salman' #It won't access to the constructor
# emp_1 = Employee('Salman', 'Khan') # It will access to the constructor
print(emp_1.first)
print(emp_1.fullname())
print(emp_1.email)


