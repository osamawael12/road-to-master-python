# 10 - Iterators

An Iterator is an object that allows us to traverse data one
element at a time.

## iter()

Converts an iterable into an iterator.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)
next()

Returns the next value.

next(iterator)

Output:

10
20
30

After the last element:

StopIteration
Iterable vs Iterator

Iterable:

Can be looped over
Examples: List, Tuple, String

Iterator:

Produces values using next()
Generators

Every Generator is an Iterator.

Data Analysis Connection

Iterators are useful for:

Large datasets
Streaming
ETL
File processing
Memory-efficient pipelines