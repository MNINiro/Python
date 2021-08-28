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

class Developer(Employee):
     raise_amt = 1.10

emp_1 = Employee('Labib', 'Rahman', 5000)
emp_2 = Employee('Test', 'User', 6000)

dev_1 = Developer('Samin', 'Islam', 50000)
dev_2 = Developer('Fuad', 'Hassan', 60000)

#print(help(Developer))
print(dev_1.email)
print(dev_2.email)
print()

print(dev_1.fullname())
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print()

print(dev_2.fullname())
print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)



