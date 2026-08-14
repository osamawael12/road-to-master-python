# 01 - NumPy Fundamentals

## What is NumPy?

NumPy is a Python library for numerical computing.

It provides:

- Arrays
- Fast mathematical operations
- Linear algebra
- Statistics
- Random numbers
- Numerical processing

## Import

```python
import numpy as np
Creating Arrays
numbers = np.array([10, 20, 30, 40])
2D Arrays
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
Important Properties
numbers.shape
numbers.ndim
numbers.size
numbers.dtype
Indexing
numbers[0]
numbers[-1]

2D:

matrix[0, 1]
Slicing
numbers[1:4]
Vectorized Operations
numbers + 10
numbers * 2
numbers / 2
numbers ** 2
Useful Functions
np.zeros(5)
np.ones(5)
np.arange(1, 10)
np.linspace(0, 1, 5)
Aggregations
numbers.sum()
numbers.mean()
numbers.min()
numbers.max()
Data Analysis Connection

NumPy is the foundation of:

Pandas
Data Analysis
Machine Learning
Scientific Computing
AI