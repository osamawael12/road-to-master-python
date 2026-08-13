
### `examples.py`

```python
# Positional arguments

def calculate_profit(sales, cost):
    return sales - cost


print(calculate_profit(500000, 320000))


# Multiple parameters

def employee_info(name, department, salary):
    return f"{name} - {department} - {salary}"


print(employee_info("Osama", "Analytics", 15000))


# Default parameter

def greet(name="User"):
    print(f"Hello {name}")


greet()
greet("Osama")


# Keyword arguments

def calculate_margin(sales, cost):
    profit = sales - cost
    return profit / sales * 100


print(calculate_margin(sales=500000, cost=320000))


# Data Analyst Example

def calculate_net_sales(price, quantity, discount=0):
    gross_sales = price * quantity
    discount_amount = gross_sales * discount / 100

    return gross_sales - discount_amount


print(calculate_net_sales(1000, 10))
print(calculate_net_sales(1000, 10, 15))