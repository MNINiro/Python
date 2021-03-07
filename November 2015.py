class StockItem:
    def __init__(self, Title, DateAcquired, Onloan):
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__Onloan = Onloan

    def getTitle(self):
        return self.__Title

    def ShowDateAcquired(self):
        return self.__DateAcquired

    def ShowOnloan(self):
        return self.__Onloan

class Book(StockItem):
    def __init__(self, Title, DateAcquired, Onloan, Author, ISBN ):
        # super().__init__(Title, DateAcquired , Onloan)  #why StockItem cant be used?
        StockItem.__init__(self,Title, DateAcquired, Onloan)
        self.__Author = Author
        self.__ISBN = ISBN

    def ShowAuthor(self):
        return self.__Author

    def ShowISBN(self):
        print(self.__ISBN)

a = Book("Computers", "12/11/2001", False, "A.Nyone", "099111")

print(a.getTitle())
print(a.ShowDateAcquired())
print(a.ShowAuthor())
print(a.ShowOnloan())

a.ShowISBN()
