# Composition: In this method, Employee class deligates some tasks to Salary class
#Salary is the part of Employee. It is "part of" relationship.
class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus) #it is instantiated Salary class inside the Employee class.
                                             # Here, Employee class is the container

    def total_salary(self):
        return self.obj_salary.annualSalary()

emp = Employee('Sam',25,20000,8000)
print(emp.total_salary())

# Aggregation: It's unidirectional. One object depends on another. if one die other one will not survive.
# here, salary is not part of the employee class. It just pass salary to Employee class
# it is "has a" relationship.

class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.obj_salary = salary; #instead of using Salary class, we are passing an instance of the Salary class

    def total_salary(self):
        return self.obj_salary.annualSalary()

salary = Salary(20000,8000)
emp = Employee('Sam',25,salary) #Relationship: Employee has a salary. It's uni-direction, salary object passed only to Employee class
print(emp.total_salary())

