from abc import ABC, abstractmethod
from dataclasses import dataclass


# Exercise 01

class DataSource(ABC):

    @abstractmethod
    def fetch(self):
        pass


# Exercise 02

class CSVDataSource(DataSource):

    def fetch(self):
        return "Fetching data from CSV"


source = CSVDataSource()

print(source.fetch())


# Exercise 03 + 04

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"

    def __eq__(self, other):
        return self.price == other.price


product1 = Product("Laptop", 25000)
product2 = Product("Computer", 25000)

print(product1)
print(product1 == product2)


# Exercise 05

@dataclass
class Customer:
    name: str
    age: int
    country: str
    sales: float


customer = Customer(
    "Osama",
    25,
    "Egypt",
    100000
)

print(customer)