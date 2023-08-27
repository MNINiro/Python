# Private variable

class person:
    def __init__(self):     # constructor
        self.A = "Armeen"  # Public / Global variable
        self._B = "Muntahi"
        self.__C = 'Nihal' # Private / Local variable

        # Add “__” in front of the variable and function
        # name can hide them when accessing them from
        # out of class.

    @property
    def printName(self):
        print(self.A)
        print(self.__C)  # Invoke private variable in a public function to access to that variable
        print(self.A, self._B, self.__C)


p = person()

# print(p.A)  # Access public variable out of class, succeed
# print(p._B)
# print(p.__C) # Access private variable out of class, fail

# x = p.printName('Omar')
# print(x)

print(p.printName)  # Access public function but this function access
#  Private variable __B successfully since
#  they are in the same class.

