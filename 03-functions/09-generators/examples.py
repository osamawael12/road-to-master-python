
### `examples.py`

# Basic Generator

def numbers():
    yield 1
    yield 2
    yield 3


for number in numbers():
    print(number)


# Generator with range

def count_up_to(n):
    number = 1

    while number <= n:
        yield number
        number += 1


for number in count_up_to(5):
    print(number)


# Generator Expression

squares = (x ** 2 for x in range(5))

for square in squares:
    print(square)


# Data Analysis Example

def read_sales(sales):
    for sale in sales:
        yield sale


sales = [10000, 25000, 50000, 75000]

for sale in read_sales(sales):
    print(sale)