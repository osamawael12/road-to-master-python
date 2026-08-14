
### `examples.py`

```python
# Higher-Order Function

def apply_operation(func, value):
    return func(value)


def square(x):
    return x ** 2


print(apply_operation(square, 5))


# Using Lambda

print(
    apply_operation(
        lambda x: x * 10,
        7
    )
)


# Function returning function

def multiplier(factor):

    def multiply(value):
        return value * factor

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))


# Data Analyst Example

def create_discount(discount):

    def apply_discount(price):
        return price * (1 - discount)

    return apply_discount


discount_10 = create_discount(0.10)

print(discount_10(1000))