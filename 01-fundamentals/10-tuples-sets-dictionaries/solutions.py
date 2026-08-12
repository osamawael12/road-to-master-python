
### `solutions.py`

```python
# Exercise 01
customer = ("Osama", 25, "Data Analyst")

print(customer)


# Exercise 02
skills = {"Python", "SQL", "Power BI", "Python", "SQL"}

print(skills)


# Exercise 03
employee = {
    "name": "Osama",
    "age": 25,
    "department": "Analytics",
    "salary": 15000
}

print(employee)


# Exercise 04
employee["experience"] = 3

print(employee)


# Exercise 05
employee["salary"] = 18000

print(employee)


# Exercise 06
customer = {
    "name": "Ahmed",
    "sales": 80000
}

if customer["sales"] >= 50000:
    print("VIP")
else:
    print("Regular")