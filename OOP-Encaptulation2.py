class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful! New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal successful! New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance


my_account = BankAccount(100)
my_account.deposit(50)  # Deposit successful! New balance: 150
my_account.withdraw(20)  # Withdrawal successful! New balance: 130
print(my_account.get_balance())  # 130
