
### `examples.py`

sales = [10000, 25000, 15000, 30000, 45000]

# Indexing
print(sales[0])
print(sales[-1])

# Slicing
print(sales[1:4])

# Modify
sales[0] = 12000

# Methods
sales.append(50000)
sales.insert(1, 18000)
sales.remove(15000)

removed = sales.pop()

sales.sort()
print(sales)

sales.reverse()
print(sales)

# Nested Lists
employees = [
    ["Ahmed", 15000],
    ["Mohamed", 18000],
    ["Ali", 22000]
]

print(employees[0])
print(employees[0][0])

# List Comprehension
high_sales = [sale for sale in sales if sale >= 20000]

print("High Sales:", high_sales)

# Data Analyst Example
sales = [10000, 25000, 5000, 45000, 30000]

total = sum(sales)
average = total / len(sales)

print("Total:", total)
print("Average:", average)