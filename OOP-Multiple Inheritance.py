# Method Resolution Order (MRO)
# In the multiple inheritance scenario members of class are searched first in the
# current class. If not found, the search continues into parent classes in depth-
# first, left to right manner without searching the same class twice.
# Search for the child class before going to its parent class.
# When a class is inherited from several classes, it searches in the order from
# left to right in the parent classes.
# It will not Visit any class more than once which means a class in the
# inheritance hierarchy is traversed only once exactly.

class Father:
    def __init__(self):
        super().__init__() #calling parents class constructor
        print("Father Class Constructor")

    def show(self):
        print("Father Class Method")

class Mother:
    def __init__(self):
        #super().__init__() #calling parents class constructor
        print("Mother Class Constructor")

    def show(self):
        print("Mother Class Method")

class Son(Father,Mother):
    def __init__(self):
        super().__init__() #calling parents class constructor. First Mother then father
        print("Son Class Constructor")

    def show(self):
        print("Son Class Method")
s = Son()
s.show() # it will call only father class constructor. To call all parents we need to use super() in all paernts classes.

# The search will start from Son. As the object of Son is
# created, the constructor of Son is called.

# Son has super()._init_() inside his constructor so its
# parent class, the one in the left side ‘Father’ class’s
# constructor is called.

# Father class also has super()._init_() inside his
# constructor so its parent ‘object’ class’s constructor is called.

# Object does not have any constructor so the search will
# continue down to right hand side class (Mother) of object
# class so Mother class’s constructor is called.

# As Mother class also has super()._inti_() so its parent
# class ‘object’ constructor is called but as object class
# already visited, the search will stop here.

#Mother -> Father -> Son