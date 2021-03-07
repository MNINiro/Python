class Army:                     #Outer class
    def __init__(self):
        self.name = 'Emmy'
        self.gn = self.Gun()    #creating inner class object

    def show(self):
        print('Name:',self.name)

    class Gun:                  #Nested class
        def __init__(self):
            self.name = 'AK47'
            self.capacity = '75 Rounds'
            self.length = '34.3 Inch'

        def display(self):
            print('Gun name:', self.name)
            print('Capacity:', self.capacity)
            print('Length:', self.length)

a = Army()
print(a.name)       # name from constructor
a.show()            # name from show method
print()

ga = a.Gun()         # creating instance of the nested class
ga.display()         # calling display method of the nested class.
print()

g = a.gn            # it will access to the nested class object of the main class
print(g.name)
print(g.capacity)
print(g.length)
print()

g.display()

x = Army().Gun().display()
print(x)
y = Army().Gun().name
print(y)