# 05 - Comprehensions

Comprehensions provide a concise way to create collections.

## List Comprehension

```python
squares = [x ** 2 for x in range(10)]
With Condition
high_sales = [x for x in sales if x >= 50000]
Dictionary Comprehension
squares = {x: x ** 2 for x in range(5)}
Data Analysis

Comprehensions are useful for:

Filtering
Transformation
Feature Engineering
Data Preparation