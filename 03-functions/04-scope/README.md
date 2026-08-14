# 04 - Scope

## Local Scope

A variable created inside a function is local.

```python
def calculate():
    sales = 50000
    print(sales)

sales cannot normally be accessed outside the function.

Global Scope

A variable created outside functions is global.

sales = 50000

def show_sales():
    print(sales)
global

global allows a function to modify a global variable.

counter = 0

def increase():
    global counter
    counter += 1
nonlocal

nonlocal allows an inner function to modify a variable from its enclosing function.

LEGB

Python searches variables in this order:

Local
Enclosing
Global
Built-in
Data Analysis Connection

Scope is important when building:

Data pipelines
Reusable functions
Configuration systems
ML workflows
Large Python applications