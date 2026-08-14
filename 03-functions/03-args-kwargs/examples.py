
### `examples.py`

```python
# *args

def calculate_total(*numbers):
    return sum(numbers)


print(calculate_total(10, 20, 30))
print(calculate_total(10, 20, 30, 40, 50))


# *args with loop

def calculate_average(*numbers):
    return sum(numbers) / len(numbers)


print(calculate_average(10, 20, 30, 40))


# **kwargs

def employee_info(**employee):
    print(employee)


employee_info(
    name="Osama",
    department="Analytics",
    salary=15000
)


# Loop through kwargs

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_info(
    name="Osama",
    experience=3,
    skill="Python"
)


# Combining

def report(title, *values, **metadata):
    print("Title:", title)
    print("Values:", values)
    print("Metadata:", metadata)


report(
    "Sales Report",
    10000,
    20000,
    30000,
    department="Sales",
    year=2026
)