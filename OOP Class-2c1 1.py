#inheritance
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

class Developer(Employee):      # its a sub class
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # it will inherit from its super class Employee
                    # or we can write
                    # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer('Tasnim', 'Shah', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')


print(dev_1.email)
print(dev_1.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.pay)


##apply_raise(self)
##fullname(self)

