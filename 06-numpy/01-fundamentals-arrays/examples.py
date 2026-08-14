
### `examples.py`

```python
import numpy as np


# 1D Array

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)


# 2D Array

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)


# Properties

print(numbers.shape)
print(numbers.ndim)
print(numbers.size)
print(numbers.dtype)


# Indexing

print(numbers[0])
print(numbers[-1])

print(matrix[0, 1])


# Slicing

print(numbers[1:4])


# Vectorized Operations

print(numbers + 10)
print(numbers * 2)
print(numbers / 2)
print(numbers ** 2)


# Useful Arrays

print(np.zeros(5))
print(np.ones(5))
print(np.arange(1, 10))
print(np.linspace(0, 1, 5))


# Aggregations

print(numbers.sum())
print(numbers.mean())
print(numbers.min())
print(numbers.max())


# Boolean Filtering

sales = np.array([
    10000,
    25000,
    50000,
    75000,
    100000
])

print(sales[sales >= 50000])