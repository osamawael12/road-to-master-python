# 03 - Abstraction, Dunder Methods & Dataclasses

## Abstraction

Abstraction defines what a class must do without exposing
implementation details.

Python provides abstraction using `ABC` and `abstractmethod`.

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):

    @abstractmethod
    def process(self):
        pass

A child class must implement process().

Dunder Methods

Dunder = Double Underscore.

Examples:

__init__
__str__
__repr__
__len__
__eq__
str

Controls the human-readable representation.

def __str__(self):
    return self.name
len

Allows len(object).

def __len__(self):
    return len(self.data)
eq

Controls equality between objects.

Dataclasses

dataclass automatically generates common methods such as
__init__, __repr__, and __eq__.

from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    sales: float
customer = Customer("Ahmed", 50000)
Data / AI Connection

Useful for:

Data models
API schemas
ETL objects
Configuration
ML pipelines
AI application data structures