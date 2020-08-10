import datetime

class LibraryItem:
    def __init__(Self, t, a, i):
        Self.__title = t
        Self.__author = a
        Self.__itemid = i
        Self.__onloan = False
        Self.__duedate = datetime.date.today()


    def GetTitle(Self):
        return(Self.Title)


    def Borrowing(Self):
        Self.__onloan = True
        Self.__duedate = Self.__duedate + datetime.timedelta(weeks=3)


    def Returning(Self):
        Self.__onloan = False


    def PrintDetails(Self):
        print(Self.__title,'; ',Self.__author,'; ',end='')
        print(Self.__itemid,'; ',Self.__onloan,'; ',Self.__duedate)      
        
       
class Book(LibraryItem):
    
    def __init__(Self, t, a, i):
        LibraryItem.__init__(Self, t, a, i)
        Self.__IsRequested = False
        Self.__RequestedBy = 0
              
    def GetIsRequested(Self): 
       return (Self.__IsRequested)
              
    def SetIsRequested(self):
        self.__IsRequested = True


class CD(LibraryItem):
              
    def  __init__(self, t, a, i): 
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    def GetGenre(self ):
       return (self.__Genre)

    def SetGenre(self, g):
     self.__Genre = g

book_1 = LibraryItem("The Origin", "Dan Brown")
book_1 = LibraryItem("0012223", "True")

print(PrintDetails())
              

        
