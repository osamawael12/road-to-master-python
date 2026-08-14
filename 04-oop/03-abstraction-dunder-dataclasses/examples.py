
### `examples.py`

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass


# =========================
# Abstraction
# =========================

class DataProcessor(ABC):

    @abstractmethod
    def process(self, data):
        pass


class SalesProcessor(DataProcessor):

    def process(self, data):
        return [x * 0.9 for x in data]


processor = SalesProcessor()

print(processor.process([100, 200, 300]))


# =========================
# Dunder Methods
# =========================

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

    def __eq__(self, other):
        return self.price == other.price


product1 = Product("Laptop", 25000)
product2 = Product("Mouse", 500)

print(product1)
print(repr(product1))
print(product1 == product2)


# =========================
# Dataclass
# =========================

@dataclass
class Customer:
    name: str
    sales: float
    country: str


customer = Customer(
    "Ahmed",
    75000,
    "Egypt"
)

print(customer)