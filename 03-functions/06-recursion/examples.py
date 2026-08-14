
### `examples.py`

```python
# Countdown

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)


countdown(5)


# Factorial

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


# Sum from 1 to n

def recursive_sum(n):
    if n == 0:
        return 0

    return n + recursive_sum(n - 1)


print(recursive_sum(5))


# Fibonacci

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))