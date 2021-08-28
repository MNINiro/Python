class Member(object):
    def __init__(self, Fname, Lname, DOB, GenderVal):
        self.Fname = Fname
        self.Lname = Lname
        self.DOB = DOB
        self.Gender = GenderVal

    def IntoductionA(self):
        return ("Hello, i am {} {}".format(self.Fname , self.Lname))

    def DisplayFullnameAndDOB(self):
        print(f"{self.Fname} {self.Lname} {self.DOB}")

class Competitor(Member):
    def __init__(self, Fname, Lname, DOB, GenderVal, Mysport):
        super().__init__(Fname, Lname, DOB, GenderVal)
        self.__sport = Mysport

    def IntroductionB(self):
        print(f"Hello, I am {self.Fname} {self.Lname} and my sport is {self.__sport}")

class official(Member):
    def __init__(self, Fname, Lname, DOB, GenderVal, trained, title):
        Member.__init__(self, Fname, Lname, DOB, GenderVal)
        self.__trained = trained
        self.__title = title

AJAWrestler = Competitor("Natale", "Beyaris", "31/05/2001" , "Female", "Wrestler")
print(AJAWrestler.IntroductionB())
print()

BMXJudge = official("Samantha", "Fairchild", "09/05/2009", "Female", "True", "Judge")
print(BMXJudge.IntoductionA())
print(BMXJudge.DisplayFullnameAndDOB())


