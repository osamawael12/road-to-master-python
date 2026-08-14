
### `examples.py`

```python
# Inheritance

class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        return "General work"


class DataAnalyst(Employee):

    def work(self):
        return "Analyzing data"


class DataEngineer(Employee):

    def work(self):
        return "Building data pipelines"


analyst = DataAnalyst("Ahmed")
engineer = DataEngineer("Ali")

print(analyst.name)
print(analyst.work())

print(engineer.name)
print(engineer.work())


# Encapsulation

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


account = BankAccount(10000)

account.deposit(5000)

print(account.get_balance())


# Polymorphism

employees = [
    DataAnalyst("Ahmed"),
    DataEngineer("Ali")
]

for employee in employees:
    print(employee.work())