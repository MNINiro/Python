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

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    
    def __mul__(self, other):
        return self.pay * other.pay
emp_1 = Employee('Lamia', 'Hossain', 50000)
emp_2 = Employee('Yasin', 'Musa', 60000)
emp_3 = Employee('Basma', 'Islam', 35000)

# It's not a magic/dunder method
# print(Employee.__add__(emp_1, emp_2)) #adding both of the employees' salaries

# Magic methods
print(emp_1 + emp_2) #adding both of the employees' salaries
print(len(emp_2))
print(emp_1 * emp_3)






