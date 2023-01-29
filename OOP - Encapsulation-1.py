# Private variable

class person:
    def __init__(self):
        self.A = "Armeen"   # Public / Global variable
        self.__B = "Niloy"  # Private / Local variable

               # Add “__” in front of the variable and function
               # name can hide them when accessing them from
               # out of class.

    @property
    def printName(self):
        print (self.A)
        print (self.__B) # Invoke private variable in a public function to access to that variable
        print (self.A, self.__B)

        
p = person()

print(p.A)    # Access public variable out of class, succeed
# print(p.__B) # Access private variable out of class, fail

print(p.printName) #  Access public function but this function access
                     #  Private variable __B successfully since 
                     #  they are in the same class.
