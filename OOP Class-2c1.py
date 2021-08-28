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

    def __init__(self, first, last, pay, prog_lang, experience):
       # Employee.__init__(self, first, last, pay)
       # or we can write
       super().__init__(first, last, pay) # it will inherit from its super class Employee
       self.prog_lang = prog_lang
       self.experience = experience

dev_1 = Developer('Fuad', 'Ahmed', 50000, 'Python', '3 years')
dev_2 = Developer('MNI', 'Niro', 60000, 'Java', '5 years')


print(dev_1.email)
print(dev_1.prog_lang)
print(dev_1.experience)
print(dev_1.pay)

dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.pay)



