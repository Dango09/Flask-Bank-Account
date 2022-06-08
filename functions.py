# child class
class Bank():
    def __init__(self):
        # super().__init__()
        self.balance = 0
        self.amount = 0
        self.loanamount = 0
        self.rate = 0
        self.period = 0

    def deposit(self,amt):
        self.amount = int(amt)
        self.balance = self.balance + self.amount
        return 'Available balance = ' + str(self.balance)

    # def withdraw(self, amount):
    #     self.amount = int(amount)
    #     if self.amount > self.balance:
    #         return "Withdraw amount = " + str(amount) + "\n" + "Insufficient balance! PLease try again! Available: " + str(self.balance)
    #     else:
    #         self.balance = self.balance - self.amount
    #         return 'Net Available Balance = ' + str(self.amount)

    def withdraw(self, amount):
        self.amount = int(amount)
        if self.balance >= self.amount:
            self.balance -= self.amount
            return "You Withdrew: " + str(self.amount) + "\n" + "Your balance is " + str(self.balance)
        else:
            return "Insufficient balance! PLease try again :("



    def bankloan(self,loanamount, rate, period):
        self.loanamount = int(loanamount)
        print("Loan taken = ", self.loanamount)
        self.rate = int(rate)
        self.period = int(period)
        si = (self.loanamount * self.rate * self.period) / 100
        a1 = self.loanamount + si
        return "Final Amount = " + str(round(a1,1)) + "\n" + "Simple Interest: " + str(round(si, 2))

    def view_money(self):
        return str(self.balance)