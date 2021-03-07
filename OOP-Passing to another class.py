class Student:
    def __init__(self,n,r):
        self.name = n
        self.roll = r

    #instance method
    def display(self):
        print("Student Name:", self.name)
        print("Student Roll:", self.roll)

class User:
    @staticmethod
    def show(s): #now, s is holding std object. So we can use all of the methods of the Student class.
        print("User Name:",s.name)
        print('Serial Number:',s.roll)

        print()
        print('=== Importing an entire method from another (Student) class ===')
        s.display() #It will import an entire method from another class

print('=== Object std will pass to the staticmethod of another class ===')
std = Student('Sami',101)
User.show(std) # object std will pass to the staticmethod of another class

print()
print('=== Output from native class ===')
std.display() #output from native class
