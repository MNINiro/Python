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

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # it will inherit from its super class Employee
                    # or we can write
                    # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):      # its a sub class
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay) # it will inherit from its super class Employee

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):     #method
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):  #method
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            
                
dev_1 = Developer('MNI', 'Niro', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Samin', 'Islam', 90000, [dev_1])


print(isinstance(mgr_1, Manager)) # isinstance and issubclass is a builtin 
                                  # function. isinstance defines object of
                                  # an instance of a class
    
print(isinstance(mgr_1, Developer))

print(isinstance(dev_1, Developer))
    
print(issubclass(Manager, Employee))

print(issubclass(Manager, Developer))




