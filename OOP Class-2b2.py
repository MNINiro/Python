class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):  #Constructor
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
    def set_raise_amt(cls,  amount): #cls is a class variable
        cls.raise_amt = amount #parameter which will take amount value,i.e 1.05
        
emp_1 = Employee('Labib', 'Rahman', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(emp_1.apply_raise())
print(emp_1.pay)

emp_str_1 = 'Tasdeeq Jawad 70000'
emp_str_2 = 'Tanjeel-Rahman-30000'
emp_str_3 = 'Samin.Islam.90000'

first, last, pay = emp_str_3.split('.') # It's an alternative constructor

new_emp_1 = Employee(first, last, pay) #It has been created by the previous line
print(new_emp_1.first)
print(new_emp_1.last)
print(new_emp_1.pay)
print(new_emp_1.email)
new_emp_1.apply_raise()
print(new_emp_1.pay)
print(new_emp_1.fullname())

first, last, pay = emp_str_2.split('-') # It's an alternative constructor
new_emp_2 = Employee(first, last, pay) #It has been created by the previous line
print(new_emp_2.email)
print(new_emp_2.pay)
print(new_emp_2.apply_raise())
print(new_emp_2.pay)