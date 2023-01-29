# Composition: In this method, Employee class delegates some tasks to Salary class
# Salary is the part of Employee. It is "part of" relationship.
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)  # it is instantiated Salary class inside the Employee class.
        # Here, Employee class is the container

    def total_salary(self):
        return self.obj_salary.annualSalary()


emp = Employee('Sam', 25, 20000, 8000)
print("Actual Salary:", emp.obj_salary.pay)  # as an object of the Salary class
print("Bonus amount:", emp.obj_salary.bonus)  # as an object of the Salary class
print("Total Salary:", emp.total_salary())


# Aggregation: It's unidirectional. One object depends on another.
# if one die other one will not survive.
# here, salary is not part of the employee class.
# It just passes salary to Employee class
# it is "has a" relationship.

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age

        # instead of using Salary class,
        # we are passing an instance of the Salary class
        self.obj_salary = pay

    def total_salary(self):
        return self.obj_salary.annualSalary()


pay = Salary(20000, 8000)

# Relationship: Employee has a salary.
# It's uni-direction, salary object passed only to Employee class
emp = Employee('Sam', 25, pay)
print(emp.total_salary())

