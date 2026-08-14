
### `examples.py`

```python
from functools import wraps
import time


def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running: {func.__name__}")

        result = func(*args, **kwargs)

        print("Completed")

        return result

    return wrapper


@logger
def calculate_profit(sales, cost):
    return sales - cost


print(calculate_profit(500000, 320000))


def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"Execution time: {end - start:.6f}s")

        return result

    return wrapper


@timer
def calculate_total(numbers):
    return sum(numbers)


print(calculate_total(range(1000000)))