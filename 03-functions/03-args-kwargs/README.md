# 03 - *args & **kwargs

## *args

Allows a function to accept any number of positional arguments.

```python
def total(*args):
    return sum(args)
total(10, 20, 30, 40)

Inside the function, args is a Tuple.

**kwargs

Allows a function to accept any number of keyword arguments.

def employee(**kwargs):
    print(kwargs)

Inside the function, kwargs is a Dictionary.

Data Analysis Connection

Useful when:

Functions need flexible inputs
Building reusable utilities
Processing dynamic configurations
Building APIs
Creating ML/Data pipelines