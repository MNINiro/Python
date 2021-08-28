# Property Decorators - Getters, Setters, and Deleters 
class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
       # self.email = first + '.' + last + '@outlook.com'

    @property
    def email(self):
        return '{}.{}@outlook.com'.format(self.first, self.last)
                      
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name deleted!')
        self.first = ""
        self.last = ""

emp_1 = Employee('John', 'Smith')
 
emp_1.fullname = 'Salman Khan'  # it will show error messsage unless

                                  # we need to use
                                  # @fullname.setter decorators

print(emp_1.first)
print(emp_1.email) # it will show only memory address. to solve this problem
                    # we need to use @property method

print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)



