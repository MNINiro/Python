class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(int(self.pay) * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):  # cls is class variable
        cls.raise_amt = amount  # parameter which will take amount value,i.e 1.05.

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split(',')
        return cls(first, last, pay)  # Here cls is the Employee class


emp_str_1 = 'Tasdeeq,Jawad,70000'
emp_str_2 = 'Tanjeel,Rahman,30000'
emp_str_3 = 'Samin,Islam,90000'

new_emp = Employee.from_string(emp_str_1)

print(new_emp.pay)
print(new_emp.email)
print(new_emp.fullname())
new_emp.apply_raise()
print(new_emp.pay)
