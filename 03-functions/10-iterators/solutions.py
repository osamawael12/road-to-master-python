# Exercise 01

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(iterator)


# Exercise 02

print(next(iterator))
print(next(iterator))


# Exercise 03

text = "DATA"

iterator = iter(text)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Exercise 04

def numbers_generator():
    yield 100
    yield 200
    yield 300


generator = numbers_generator()

print(next(generator))
print(next(generator))
print(next(generator))


# Exercise 05

# Iterable:
# An object that can be iterated over.

# Iterator:
# An object that produces values using next().

# Generator:
# A special type of Iterator created using yield.