class Employee:

    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay): #__ is called dunder method
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
        Employee.num_of_emps += 1
        
    def fullname(self): #regular method, self is an Instants variable
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)   

    @classmethod    #Its a decorator. @classmethod helps to create objects in multiple ways 
    def set_raise_amt(cls, amount): #cls is class variable
        cls.raise_amt = amount #parameter which will take amount value,i.e 1.05
                               # #Here cls is the Employee class
        


Employee.set_raise_amt(1.05) #Its a classmethod

    # It is equal to Employee.raise_amt = 1.05
    #or
    #emp_1.set_raise_amt(1.05)


emp_1 = Employee('Labib', 'Rahman', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(Employee.raise_amt)
print(emp_1.apply_raise())
print(emp_1.pay)

