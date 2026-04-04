class BankAccount: #parent class
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    
    def withdraw(self, amount):
        self.balance-= amount


class SavingsAccount(BankAccount): #child class
    def __init__(self, min_balance):
        self.balance = 0
        self.min_balance = min_balance

    
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


savings_account = SavingsAccount(200)
savings_account.deposit(1500)
savings_account.withdraw(500)
savings_account.withdraw(900)