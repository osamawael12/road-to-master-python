# 08 - Decorators

A Decorator is a function that modifies or extends another function.

## Basic Example

```python
def logger(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished...")

    return wrapper

Apply:

@logger
def process_data():
    print("Processing data")
Decorator with Arguments
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        result = func(*args, **kwargs)
        print("Completed")
        return result

    return wrapper
Data Analysis / AI Connection

Decorators are useful for:

Logging
Timing functions
Validation
Authentication
Monitoring
API development
ML pipeline monitoring