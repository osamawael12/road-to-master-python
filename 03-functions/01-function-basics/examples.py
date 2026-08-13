
### `examples.py`

```python
# Basic function

def greet():
    print("Hello, Data Analyst!")


greet()


# Parameter

def greet_user(name):
    print(f"Hello {name}")


greet_user("Osama")


# Multiple parameters

def calculate_profit(sales, cost):
    return sales - cost


profit = calculate_profit(500000, 320000)

print("Profit:", profit)


# Data Analyst Example

def calculate_margin(sales, cost):
    profit = sales - cost
    return profit / sales * 100


margin = calculate_margin(500000, 320000)

print("Margin:", margin)