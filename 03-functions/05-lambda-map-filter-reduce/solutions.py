from functools import reduce


# Exercise 01

square = lambda x: x ** 2

print(square(5))


# Exercise 02

numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda x: x ** 2, numbers)
)

print(squares)


# Exercise 03

greater_than_three = list(
    filter(lambda x: x > 3, numbers)
)

print(greater_than_three)


# Exercise 04

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)


# Exercise 05

sales = [10000, 25000, 50000, 75000, 100000]

high_sales = list(
    filter(lambda sale: sale >= 50000, sales)
)

print(high_sales)


# Exercise 06

discounted_sales = list(
    map(lambda sale: sale * 0.90, sales)
)

print(discounted_sales)