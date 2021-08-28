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

    def __init__(self, first, last, pay, prog_lang, experience):
        # Employee.__init__(self, first, last, pay)
        # or we can write
        super().__init__(first, last, pay)  # it will inherit from its super class Employee
        self.prog_lang = prog_lang
        self.experience = experience

class Manager(Employee):      # its a sub class
    def __init__(self, first, last, pay, employees=None): # Here None is the defult argument
        super().__init__(first, last, pay) # it will inherit from its super class Employee

        if employees is None:
            self.employees = [] 
        else:
            self.employees = employees # Add Employee list here

    def add_emp(self, emp):     #method
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):  #method
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            
                
dev_1 = Developer('Fuad', 'Ahmed', 50000, 'Python', '3 years')
dev_2 = Developer('MNI', 'Niro', 60000, 'Java', '5 years')

mgr_1 = Manager('Samin', 'Islam', 90000, [dev_1])   # this mgr_1 supervises dev_1.
                                                     # It will inherit all of the
mgr_1.print_emps() # It will print out full name of the employee that supervised by this manager
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
#
# print()
#
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()





