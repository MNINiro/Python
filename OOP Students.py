class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours


aStudent = Student("Adams, Henry", 127, 228)


print ("Name     :", aStudent.getName())
print ("Hours    :", aStudent.getHours())
print ("Q Points :", aStudent.getQPoints())
print ("GPA      :", aStudent.gpa())
