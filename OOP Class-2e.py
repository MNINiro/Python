# Property Decorators - Getters, Setters, and Deleters 

class Employee:

    raise_amt = 1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@outlook.com'

    def fullname(self,x):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
 
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

emp_1.first = 'Salman'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())



