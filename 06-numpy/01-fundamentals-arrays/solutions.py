import numpy as np


# Exercise 01

numbers = np.array([
    10, 20, 30, 40, 50
])

print(numbers)


# Exercise 02

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)


# Exercise 03

print(numbers.shape)
print(numbers.ndim)
print(numbers.size)
print(numbers.dtype)


# Exercise 04

print(numbers[0])
print(numbers[-1])


# Exercise 05

print(matrix[1, 2])


# Exercise 06

print(numbers * 10)


# Exercise 07

print(
    numbers[numbers > 50]
)


# Exercise 08

print(numbers.sum())
print(numbers.mean())
print(numbers.min())
print(numbers.max())