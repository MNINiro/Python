class school:
    tot = 0
    avg = 0
    raise_amount = 2

    def __init__(self,first,last):
        self.first = first
        self.last = last

    def student_table(self,first,last,sgrade,dob):
        self.first = first
        self.last = last
        self.sgrade = sgrade
        self.dob = dob

    @classmethod
    def teacher_table(self,first, last,tgrade,doj,sub_code,salary,working_years):
        self.first = first
        self.last = last
        self.tgrade = tgrade
        self.doj = doj
        self.sub_code = sub_code
        self.salary = salary
        self.working_years = working_years

    def tid(self):
        return '{}{}'.format(self.sub_code,self.doj)

    def sid(self):
        return '{}{}'.format(self.sgrade,self.dob)

    def subject(self,code,name,grade):
        self.code = code
        self.name = name
        self.grade = grade



class marks(school):
    def __init__(self,first,last,sgrade,bang,eng,phy):
        super().__init__(first, last)

        self.bang = bang
        self.eng = eng
        self.phy = phy
        self.tot = bang + eng + phy
        self.avg = self.tot/3

               
        if self.tot < 180:
            print('cannot sit for the board examination')
        elif bang <= 60:
            print('cannot sit for bangla exam in cie')
        elif eng <= 60:
            print('cannot sit for english exam in cie')
        elif phy <= 60:
            print('cannot sit for physics exam in cie')
        else:
            print('can sit for cie exam')
            

print()            

f = input('Enter First Name :')
l = input('Enter Last Name :')
g = input('Enter class :')
b = int(input('Enter bangla marks :'))
e = int(input('Enter English marks :'))
p = int(input('Enter Physics marks :'))

stud1 = marks(f,l,g,b,e,p)

print(stud1.first)
print(stud1.last)
print(stud1.bang)
print(stud1.eng)
print(stud1.phy)
print(stud1.tot)
print(stud1.avg)
            

tt = school.teacher_table('Basma','Islam','XII','16-11-2010','Chem',10000,5)              

class Msalary(school):
    
    
    def __init__(self,first,last,tgrade,doj,sub_code,salary,working_years):
        super().teacher_table(first,last,tgrade,doj,sub_code,salary,working_years)
        
     
    def apply_raise(self):
        
        if self.working_years >= 5:
            self.salary = int(self.salary * self.raise_amount)

tea2 = Msalary('alfi','islam','X','06-10-2013','phy',5000,3)


tea2.apply_raise()
print(tea2.first)
print(tea2.last)
print(tea2.tgrade)
print(tea2.doj)
print(tea2.sub_code)
print(tea2.salary)
print(tea2.working_years)



    
        
