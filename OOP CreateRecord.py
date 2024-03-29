# implement a structure similar to C struct or Pascal record using a class
# tested with Python24

class Employee(object):
    def __init__(self, name=None, dept=None, salary=2000):
        self.name = name
        self.dept = dept
        self.salary = salary

# one way to load the structure
john = Employee('Johnson', 'software', 3000)
allan = Employee('Allan', 'hardware', 3400)
mark = Employee('Mark', 'shipping/handling', 2600)
zoe = Employee('Zoe', 'wordprocessing', 2100)

# another way to load the structure
ted = Employee()
ted.name = 'Ted Tetris'
ted.dept = 'human resources'
ted.salary = 5000

# this works like a structure/record
print("%s works in %s and earns $%s/month" % (zoe.name, zoe.dept, zoe.salary))
print("%s works in %s and earns $%s/month" % (ted.name, ted.dept, ted.salary))
print('-' * 60)


# for a long list of employees you can do this
empList = [allan, john, mark, ted, zoe] #All objects are in the list

for emp in empList:
    print("%s works in %s and earns $%s/month" % \
        (emp.name, emp.dept, emp.salary))
print('=' * 60)

# ted had a name & salary change
ted.name = "Tanya Tetris"
ted.salary = 4500
print("%s works in %s and earns $%s/month" % (ted.name, ted.dept, ted.salary))
print('-'*60)

# use list comprehension to get the average salary

Total_Salary = sum([emp.salary for emp in empList])
print("Total Salary of all employees is",Total_Salary)

print("The average monthly salary of all employees: ")
average_salary = Total_Salary/len(empList)
print("Average Salary of all employees is $%0.2f" % average_salary)
