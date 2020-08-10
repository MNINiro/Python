class BankAccount:
    """ Class for Bank Accounts"""

    type = 'Normal Account'    # variable shared by all objects of the class

    def __init__(self, name):
        # default variables unique to each object:
        self.userName = name
        self.balance = 0.0

    # Object Methods:

    def showBalance(self):
        print (self.balance)
        return

    def withdrawMoney(self, amount):
        self.balance -= amount
        return

    def depositMoney(self, amount):
        self.balance += amount
        return
    
