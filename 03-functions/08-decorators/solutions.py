from functools import wraps
import time


def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Function started")

        result = func(*args, **kwargs)

        print("Function finished")

        return result

    return wrapper


@logger
def calculate_sum(a, b):
    return a + b


print(calculate_sum(10, 20))


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


print(calculate_total(range(100000)))