class Employee:

    num_of_employee = 0
    Raise_Amount = 1

    #i = int(input("Enter the number of entries to be made")
    #For 0 to i
    def __init__(Self, First, Last, Pay):
        Self.First = First 
        Self.Last = Last 
        Self.Pay = Pay
        Self.Email = Self.First + '.' + Self.Last + '@company.com'

        Employee.num_of_employee += 1

    def Fullname(Self):
        return '{} {}'.format(Self.First, Self.Last)

    def Apply_Raise(Self):
        Self.Pay = int(Self.Pay * Self.Raise_Amount)

    

class Developer(Employee):
    Raise_Amount = 1.10
    def __init__(Self, First, Last, Pay, Prog_Lang):
        super().__init__(First, Last, Pay)

        Self.Prog_Lang = Prog_Lang

class WebDeveloper(Developer):

    def __init__(Self, First, Last, Pay, Prog_Lang, Employees = None):
        super().__init__(First, Last, Pay, Prog_Lang)

        if Employees is None:
                Self.Developer = []
        else:
            Self.Developer = Developer

    def Add_Emp(Self, Emp):
        if Emp not in Self.Developer:
            Self.Developer.Append(Emp)

    def Remove_Emp(Self, Emp):
        if Emp in Self.Developer:
            Self.Developer.Remove(Emp)

    def Print_Emps(Self):
        for Emp in Self.Developer:
            print('-->', Emp.Fullname())


Dev_1 = Developer('E', 'F', 50000, 'Ruby')
Dev_2 = Developer('G', 'H', 75000, 'C#')

Manager_1 = WebDeveloper('I', 'J', 35000, 'Py', [Dev_1])



##    @classmethod
##        def from_string(cls, emp_str):
##            First, Last, Pay = emp_str.split('-')
##                return cls(First, Last, Pay)
##
##    @staticmethod
##        def is_workday(day):
##            if day.weekday() == 5 or day.weekday() == 6:
##                return Year, Month, Day, 'is a weekend'
##                return Year, Month, Day, 'is a weekday'
    
Entry1 = Employee( 'A', 'B', 75000)

emp_str_1 = 'C-D-55000'

##new_emp_1 = Employee.from_string(emp_str_1)

##Year = int(input("Enter the Year = "))
##Month = int(input("Enter the Month = "))
##Day = int(input("Enter the Day = "))
##
##
####if Year != range(1990, 2018): 
####    Inv == True
####
####    While(Inv)
####    print("Re-Enter a valid Year")
####
####    if Year == range(1990, 2018)
####        Inv == False
##
##
##    
##import datetime
##my_date = datetime.date(Year, Month, Day)
    

print(Manager_1.First)

print(Manager_1.Last)

print(Manager_1.Pay)

print(Manager_1.Email)

print(Manager_1.Prog_Lang)


Manager_1.Print_Emps

print(Dev_1.Email)

print(Dev_2.Email)


#print(Entry1.First)
#print(Entry1.Last)
#print(Entry1.Email)
#print(Entry1.Pay)
#print(new_emp_1.Pay)
#print(Employee.is_workday(my_date))
#print(Employee.num_of_employee)
