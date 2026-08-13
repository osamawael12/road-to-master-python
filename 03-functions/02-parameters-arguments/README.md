# 02 - Parameters & Arguments

## Parameters

Variables defined inside the function definition.

```python
def greet(name):
    print(f"Hello {name}")
Arguments

Values passed when calling the function.

greet("Osama")
Multiple Parameters
def calculate_profit(sales, cost):
    return sales - cost
Default Parameters
def greet(name="User"):
    print(f"Hello {name}")
Keyword Arguments
def employee(name, salary):
    print(name, salary)

employee(name="Osama", salary=15000)
Positional Arguments
employee("Osama", 15000)
Data Analysis

Parameters make functions reusable for:

KPI calculations
Data cleaning
Business rules
ETL transformations
ML preprocessing