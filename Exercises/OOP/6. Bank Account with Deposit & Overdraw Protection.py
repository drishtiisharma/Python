# Problem Statement: Write a Python program to create a BankAccount class with a balance attribute and two methods: deposit(amount) that adds funds to the balance, and withdraw(amount) that deducts funds but prevents the balance from going below zero.

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amt):
        self.balance += amt
        print("bal after depositing",amt,"=",self.balance)
    
    def withdraw(self,amt):
        if amt<= self.balance:
            self.balance -= amt
            print("bal after withdraw =",self.balance)
        else:
            print("can't withdraw more than you have!")

b = BankAccount(1000)
b.deposit(500)
b.withdraw(2000)
