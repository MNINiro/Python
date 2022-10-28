class Employee:
    def __init__(self, ename):
        self.name = ename
        self.internC = self.intern()
        self.headC = self.head()

    def show(self):
        print('Employe List')
        print('Name:', self.name)

    class intern:
        def __init__(self):
            self.name = "Smith"
            self.Id = '657'

        def display(self):
            print("Name:", self.name)
            print("Id:", self.Id)

    class head:
        def __init__(self):
            self.name = 'Auba'
            self.degree = 'BSc'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)


outer = Employee("Employee")
outer.show()

d1 = outer.internC
d2 = outer.headC
print()

d1.display()
print()

d2.display()
