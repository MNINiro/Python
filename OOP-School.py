class school:
    def __init__(self, schoolName, address):
        self.SchoolName = schoolName
        self.Address = address

    def show(self):
        print('School Name:', self.SchoolName)
        print('SAddress', self.Address)


class Teacher(school):

    def __init__(self, SchoolName, Address, first, last, TeacherID, Subject):
        super().__init__(SchoolName, Address)
        self.first = first
        self.last = last
        self.TeacherID = TeacherID
        self.subject = Subject

    def show(self):
        print('Teacher Name:', self.first, self.last)
        print('TeacherID:', self.TeacherID)
        print('Subject:', self.subject)
        print('School Name:', self.SchoolName)
        print('Address:', self.Address)


class Student(school):

    def __init__(self, SchoolName, Address, first, last, StudentID, Class):
        super().__init__(SchoolName, Address)
        self.first = first
        self.last = last
        self.StudentID = StudentID
        self.Class = Class
        self.markC = self.Marks()  # object of the inner class Marks

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    # @fullName.setter
    # def fullname(self, name):
    #     first, last = name.split(' ')
    #     self.first = first
    #     self.last = last

    def show(self):
        print('Student Name:', self.fullName)
        print('StudentID:', self.StudentID)
        print('Class:', self.Class)

    class Marks:
        def __init__(self):
            self.Physics = 0
            self.Maths = 0
            self.Chemistry = 0
            self.CS = 0

        def show(self, phy, math, chem, cse):
            print('Physics Marks:', phy)
            print('Maths Marks:', math)
            print('Chemistry Marks:', chem)
            print('Computer Science Marks:', cse)
            print()
            result = phy + math + chem + cse
            average = result / 4
            print('Total:', result)
            print('Average:', average)

            if average >= 80:
                print('A Grade')
            elif average >= 70:
                print('B Grade')
            elif average >= 60:
                print('C Grade')
            elif average >= 50:
                print('D Grade')
            else:
                print('Fail')


schName = input('Enter School Name:')
location = input('Enter Address:')
sch = school(schName, location)
sch.show()
print()

teacher = Teacher(schName, location, 'MNI', 'Niro', 10110, 'CSE')
teacher.show()
print()

student = Student(schName, location, 'Shabab', 'Ahmed', 201, 'XII')
# sname = input('Enter Student full name:')
# student.fullName = sname
student.show()
print()

grades = student.markC
ph = int(input('Enter Physics marks:'))
mh = int(input('Enter Maths marks:'))
ch = int(input('Enter Chemistry marks:'))
cs = int(input('Enter CSE marks:'))
print()
grades.show(ph, mh, ch, cs)
