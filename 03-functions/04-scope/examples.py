
### `examples.py`

```python
# Local Scope

def calculate_profit():
    sales = 500000
    cost = 320000

    return sales - cost


print(calculate_profit())


# Global Scope

company = "ABC Analytics"


def show_company():
    print(company)


show_company()


# global

counter = 0


def increase_counter():
    global counter
    counter += 1


increase_counter()
increase_counter()

print(counter)


# nonlocal

def outer():
    value = 10

    def inner():
        nonlocal value
        value += 5

    inner()

    return value


print(outer())