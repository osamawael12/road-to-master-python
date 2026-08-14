# 05 - Lambda, map, filter, reduce

## Lambda

A lambda is a small anonymous function.

```python
square = lambda x: x ** 2
map()

Applies a function to every element.

numbers = [1, 2, 3]

squares = list(map(lambda x: x ** 2, numbers))
filter()

Keeps elements that satisfy a condition.

numbers = [1, 2, 3, 4]

even = list(filter(lambda x: x % 2 == 0, numbers))
reduce()

Combines values into a single result.

from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers)
Data Analysis Connection

These concepts are useful for:

Data transformation
Filtering records
Aggregations
Feature engineering
Functional programming