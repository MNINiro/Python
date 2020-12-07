class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def printBalance(self):
        return self.balance

account = BankAccount() # creating instance
account.deposit(100)
account.deposit(100)
account.deposit(400)

print(account.printBalance())
account.withdraw(700)
print(account.printBalance())

