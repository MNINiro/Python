class Employee:

    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay): # It's a regular instance method
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   

    @classmethod
    def set_raise_amt(cls,  amount): #cls is class variable
        cls.raise_amt = amount #parameter which will take amount value,i.e 1.05

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod      # @ This decorator is used when we don't need any class instances or variables
    def is_workday(day): #@staticmethod does not take an instance or class as an argument
        if day.weekday() == 5 or day.weekday() == 6: # weekday is a predefined 
            return False                            # function where monday=0
                                                    # and sunday=6
        return True
    
    
emp_1 = Employee('Labib', 'Rahman', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2019, 12, 16)
print(Employee.is_workday(my_date))


