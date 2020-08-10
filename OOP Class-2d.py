#Special (Magic/Dunder) Methods 

class Employee:

    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
                      
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)   

   
    def __str__(self): # for more readable representation of object
        return'{}-{}'.format(self.fullname(), self.email)
        
    def __repr__(self): # this method mostly used for debugging and loging  
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

        # reprlib.repr(obj) : This is the repr() method of aRepr.
        # It returns a string similar to that returned by the built-in function
        # of the same name, but with limits on most sizes.

        
emp_1 = Employee('MNI', 'Niro', 50000)
emp_2 = Employee('Test', 'User', 60000)


##print(1 + 2) # addition. It uses dunder Add method from library
##print('a' + 'b') # concate. It uses dunder Concate method from library
##
##
print(int.__add__(1,4))
print(str.__add__('b', 'c'))
print(int.__sub__(4,2))
print(int.__mul__(2,4))
print(str.__len__('Basma'))

print(emp_1)
print(emp_2)

##print()
##
##print(str(emp_1))
##print(repr(emp_2))
##
print()

print(emp_1.__repr__())
print(emp_1.__str__())



