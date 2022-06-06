# parent class
class User:
    def __init__(self):
        self.balance = 0
        print("Hello! Welcome to the Deposit & Withdrawal Machine")

# child class
class Bank(User):
    def __init__(self):
        super().__init__()
        self.balance = 0

    def deposit(self):
        self.amount = int(amount)
        self.balance = self.balance + self.amount
        return 'Available balance =' + str(self.balance)

    def withdraw(self, amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            return "Insufficient balance! PLease try again" + str(self.balance)
        else:
            self.balance = self.balance - self.amount
            return 'Net Available Balance =' + str(self.amount)

    def view_money(self):
        return str(self.balance)