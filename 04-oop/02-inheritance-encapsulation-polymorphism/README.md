# 02 - Inheritance, Encapsulation & Polymorphism

## Inheritance

A child class can reuse attributes and methods from a parent class.

```python
class Employee:

    def work(self):
        return "Working"


class DataAnalyst(Employee):
    pass
analyst = DataAnalyst()

print(analyst.work())
Method Overriding

A child class can provide its own implementation.

class Employee:

    def work(self):
        return "General work"


class DataAnalyst(Employee):

    def work(self):
        return "Analyzing data"
Encapsulation

Encapsulation controls access to object data.

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

__salary is treated as a private attribute.

Polymorphism

Different objects can respond to the same method in different ways.

employees = [
    DataAnalyst(),
    DataEngineer()
]

for employee in employees:
    employee.work()
Data / AI Connection

These concepts are useful for:

ETL frameworks
Data pipeline components
ML model classes
API clients
AI agents
Large software systems