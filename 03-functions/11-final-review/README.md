# 11 - Function Best Practices & Final Review

## Best Practices

### 1. Single Responsibility

Each function should do one clear task.

### 2. Meaningful Names

```python
def calculate_profit():
    ...

Avoid:

def calc():
    ...
3. Use Return

Prefer returning values instead of printing inside reusable functions.

4. Avoid Global Variables

Pass data through parameters.

5. Keep Functions Small

Small functions are easier to:

Test
Debug
Reuse
Maintain
6. Type Hints
def calculate_profit(sales: float, cost: float) -> float:
    return sales - cost
7. Docstrings
def calculate_profit(sales, cost):
    """Calculate profit from sales and cost."""
    return sales - cost
Functions Covered
Function Basics
Parameters & Arguments
*args
**kwargs
Scope
Lambda
map()
filter()
reduce()
Recursion
Higher-Order Functions
Closures
Decorators
Generators
Iterators
Type Hints
Docstrings
Best Practices
Data Analysis Connection

Functions are the foundation of reusable:

Data Cleaning
ETL
KPI calculations
Feature Engineering
ML preprocessing
Automation