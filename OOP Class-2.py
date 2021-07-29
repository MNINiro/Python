class Employee:
    def __init__(self, first, last, pay): #constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Malcom', 'Holmes', 50000) #creating object
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

print('Full name:',emp_1.fullname())
print(Employee.fullname(emp_1))


