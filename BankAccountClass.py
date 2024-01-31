class bank_account():
    def __init__(self):
        self.balance = 0

    def deposite(self):
        amount = float(input("Enter the amount to be deposited :"))
        self.balance += amount
        print("Amount deposited : ",amount)
    def withdraw(self):
        amount = float(input("Enter the amount to be withdrawn :"))
        if(self.balance>=amount):
            self.balance -= amount
            print("Withdrawn :",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("Final balance :",self.balance)


s = bank_account()
s.deposite()
s.withdraw()
s.display()