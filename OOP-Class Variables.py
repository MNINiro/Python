class Mobile:
    fp = "Yes"  # It's a class variable

    def __init__(self):
        self.model = "Galaxy Note"

    def showModel(self):
        print("Model :", self.model)

    @classmethod  # It's a classmethod
    def isfp(cls):  # classmethod must use cls to access class variable
        print("Finger print:", cls.fp)


x = Mobile()  # creating instance
x.showModel()
print("FP:", x.fp)  # Now it will access to the class variable
x.isfp()  # Now it will access to the classmethod
print()

Mobile.fp = "No"  # changing the original class variable. Don't use instance.
Mobile.isfp()  # Now it will access to the classmethod after modification.
