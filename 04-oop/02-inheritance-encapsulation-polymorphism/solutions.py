# Exercise 01

class Employee:

    def work(self):
        return "General work"


# Exercise 02

class DataAnalyst(Employee):

    def work(self):
        return "Analyzing data"


# Exercise 03

class DataEngineer(Employee):

    def work(self):
        return "Building data pipelines"


# Exercise 04

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)

account.deposit(5000)
account.withdraw(2000)

print(account.get_balance())


# Exercise 05

employees = [
    DataAnalyst(),
    DataEngineer()
]

for employee in employees:
    print(employee.work())