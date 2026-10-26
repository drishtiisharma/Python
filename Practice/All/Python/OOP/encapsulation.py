'''
ENCAPSULATION
=============

groups data and related methods together while controlling how data is accessed and modified

'''

# public access
class Bank:
    def __init__(self,bal):
        self.bal = bal
    def show(self):
        print(self.bal)

b = Bank(2000)
b.show()

# getter and setters

class Bank:
    def __init__(self, bal):
        self.__bal = bal

    def get_balance(self):
        return self.__bal

    def set_balance(self, new_bal):
        if new_bal < 0:
            raise ValueError("Balance cannot be negative")
        self.__bal = new_bal


b1 = Bank(1000)

print(b1.get_balance())
b1.set_balance(500)
print(b1.get_balance())



# with decorators

class Bank:
    def __init__(self, bal):
        self.__bal = bal

    @property
    def balance(self):
        pass

    @balance.getter
    def show(self):
        return self.__bal
    
    @balance.setter
    def balance(self, new_bal):
        if new_bal < 0:
            raise ValueError("Balance cannot be negative")
        self.__bal = new_bal


b1 = Bank(1000)
print(b1.show)

b1.balance = 500
print(b1.show)