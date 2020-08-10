class school:
    tot = 0
    avg = 0

    def __init__(self,first,last):
        self.first = first
        self.last = last

    def student_table(self,first,last,sgrade,dob):
        self.first = first
        self.last = last
        self.sgrade = sgrade
        self.dob = dob

    def teacher_table(self,first,last,tgrade,doj,sub_code,salary):
        self.first = first
        self.last = last
        self.tgrade = tgrade
        self.doj = doj
        self.sub_code = sub_code
        self.salary = salary

    def tid(self):
        return '{}{}'.format(self.sub_code,self.doj)

    def sid(self):
        return '{}{}'.format(self.sgrade,self.dob)

    def subject(self,code,name,grade):
        self.code = code
        self.name = name
        self.grade = grade

class marks(school):
    def __init__(self,first,last,sgrade,dob,bang,eng,phy):
        super().__init__(first, last)

        self.bang = bang
        self.eng = eng
        self.phy = phy
        self.tot = bang + eng + phy
        self.avg = self.tot/3



stud1 = marks('basma','islam','12','07-06-2000',85,87,95)
##tea1 = school('alfi','islam','10','06-08-1990')

print(stud1.first)
print(stud1.last)
print(stud1.bang)
print(stud1.eng)
print(stud1.phy)
print(stud1.tot)
print(stud1.avg)




    
        
