# Create a BankAccount class with a private balance and methods to deposit and withdraw money.

class BankAccount:
    def __init__(self,bal):
        self.__bal = bal
        print(self.__bal)
    def deposit(self,amt):
        self.__bal += amt
        return self.__bal
    def withdraw(self,amt):
        if amt<=self.__bal:
            self.__bal -= amt
            return self.__bal
        else:
            print("cant withdraw more than you have")

print("current balance: ")
b = BankAccount(1000)
# print(b.bal) # will throw error -> private var
print("bal after depositing:",b.deposit(500))
print("bal after withdrawing",b.withdraw(200))