class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# -----------------------------
print(Employee.num_of_emps)

emp_1 = Employee('Labib', 'Rahman', 50000)
print(emp_1.num_of_emps)
print(emp_1.first)
print(emp_1.email)
print('Original pay:',emp_1.pay)

emp_1.apply_raise()
print('After raise:', emp_1.pay)
print()

Employee.raise_amount = 1.05
emp_2 = Employee('Omar', 'Ayman', 60000)
print(emp_2.num_of_emps)
print(emp_2.last)
emp_2.apply_raise()
print(emp_2.pay)
print()

emp_3 = Employee('Fuad', 'Hassan', 70000)
print(emp_3.num_of_emps)
print(emp_3.fullname())
