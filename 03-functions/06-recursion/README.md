# 06 - Recursion

## What is Recursion?

Recursion is when a function calls itself.

A recursive function needs:

1. Base Case
2. Recursive Case

## Example

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)
Factorial
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
Fibonacci
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
Data & AI Connection

Recursion is important for:

Tree traversal
Graph algorithms
Searching
Divide and conquer
Algorithms used in AI