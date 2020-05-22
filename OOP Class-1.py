class Employee:
	pass

emp_1= Employee()
emp_2 = Employee()

emp_1.first = 'Malcom'
emp_1.last = 'Holmes'
emp_1.email = 'Malcom.Holmes@outlook.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print(emp_1.email)


print(emp_1.first + emp_1.last)
