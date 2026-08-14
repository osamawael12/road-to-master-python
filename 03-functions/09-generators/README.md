# 09 - Generators

A Generator produces values one at a time instead of storing
all values in memory.

## yield

`yield` pauses the function and resumes it when the next value
is requested.

```python
def numbers():
    yield 1
    yield 2
    yield 3
Using a Generator
for number in numbers():
    print(number)
Generator Expression
squares = (x ** 2 for x in range(10))
Why Generators?

Generators are memory efficient.

They are useful for:

Large datasets
ETL pipelines
File processing
Streaming data
APIs
Machine Learning pipelines