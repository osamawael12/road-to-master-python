# 07 - Higher-Order Functions & Closures

## Higher-Order Function

A function that:

- Accepts another function as an argument
- Returns another function

## Example

```python
def apply_operation(func, value):
    return func(value)

square = lambda x: x ** 2

print(apply_operation(square, 5))
Returning Functions
def multiplier(factor):

    def multiply(value):
        return value * factor

    return multiply
Closure

A Closure is an inner function that remembers variables
from its enclosing scope.

double = multiplier(2)

print(double(10))
Data Analysis / AI Connection

Higher-order functions and closures are useful in:

Data transformations
Pipelines
Decorators
Feature engineering
ML preprocessing
Reusable utilities