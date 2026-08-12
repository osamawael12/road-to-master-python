# 01 - Lists

## Objectives

- Create Lists
- Indexing
- Slicing
- Modify elements
- List methods
- Nested Lists
- List Comprehension
- Data Analysis use cases

## Creating Lists

```python
sales = [10000, 25000, 15000]
Indexing
sales[0]
sales[-1]
Slicing
sales[1:3]
sales[:3]
sales[2:]
Common Methods
append()
insert()
remove()
pop()
sort()
reverse()
clear()
List Comprehension
sales = [10000, 25000, 15000]

high_sales = [sale for sale in sales if sale >= 20000]
Data Analysis

Lists are useful for storing and processing collections of values before using NumPy and Pandas.