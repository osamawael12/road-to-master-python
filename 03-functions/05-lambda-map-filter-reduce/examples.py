
### `examples.py`

```python
from functools import reduce


# Lambda

square = lambda x: x ** 2

print(square(5))


# map

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)


# filter

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)


# reduce

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)


# Data Analyst Example

sales = [10000, 25000, 50000, 75000, 120000]

high_sales = list(
    filter(lambda sale: sale >= 50000, sales)
)

discounted_sales = list(
    map(lambda sale: sale * 0.9, sales)
)

total_sales = reduce(
    lambda a, b: a + b,
    sales
)

print("High Sales:", high_sales)
print("Discounted:", discounted_sales)
print("Total:", total_sales)