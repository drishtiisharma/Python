# Store an employee's salary as a private attribute and provide methods to get and update the salary.

class Employee:
    def __init__(self,salary):
        self.__salary = salary
    def get_sal(self):
        return self.__salary
    def inc_sal(self,amt):
        self.__salary += amt
        return self.__salary
    def dec_sal(self,amt):
        self.__salary -= amt
        return self.__salary
    def update_sal(self,salary):
        self.__salary = salary
        return salary
    def check_sal(self,salary):
        if salary < 0:
            print("salary can't be negative")
        return self.__salary

e = Employee(20000)
print(e.get_sal())
print(e.inc_sal(1500))
print(e.dec_sal(200))
print(e.update_sal(254541))
print(e.check_sal(-1551))



