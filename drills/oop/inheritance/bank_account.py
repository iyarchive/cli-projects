class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    @property
    def status(self):
        if self.balance > 0:
            return "Active"
        else:
            return "Empty"
        
    def __str__(self):
        return f"{self.owner}'s account - ₱{self.balance} ({self.status})"
    
class SavingsAccount(BankAccount):

    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * (self.interest_rate/100)

    def __str__(self):
        return super().__str__() + f" with an interest rate of {self.interest_rate}%"
    

account1 = BankAccount("Iya")
account2 = SavingsAccount("Mary", 10)

account1.deposit(500)
account1.withdraw(30)
account1.deposit(768)
print(account1.status)
print(account1)

account2.deposit(800)
account2.withdraw(90)
account2.deposit(78)
account2.apply_interest()
print(account2.status)
print(account2)
