# Property Decorators - Getters, Setters, and Deleters 
class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property     #Getter
    def email(self):
        return '{}.{}@outlook.com'.format(self.first, self.last)
                      
    @property       #Getter
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
 
emp_1.first = 'Salman'

print(emp_1.first)
# it will show only memory address. to solve this problem
# we need to use @property method or print(emp_1.email())
print(emp_1.email)


#print(emp_1.fullname()) # same @property methos can be used before fullname
print(emp_1.fullname)






