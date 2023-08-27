class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Arghya', 'Roy', 50000)
emp_2 = Employee('Shamim', 'Islam', 60000)

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)
print(emp_1.email)
print(emp_1.fullname())

emp_1.raise_amount = 1.05
emp_1.apply_raise()
print(emp_1.pay)

emp_2.apply_raise()
print(emp_2.pay)
