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

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return'{}-{}'.format(self.fullname(), self.email)
        

        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)



##print(1 + 2) # addition

##print(int.__add__(1,2))
##print(str.__add__('a', 'b'))

      
#print('a' + 'b') # concate

print(len('Testing'))
print('Testing'.__len__())
