# Tuple

customer = ("Osama", 25, "Data Analyst")

print(customer)
print(customer[0])


# Set

skills = {"Python", "SQL", "Power BI", "Python"}

print(skills)

skills.add("Excel")
skills.remove("SQL")

print(skills)


# Dictionary

employee = {
    "name": "Osama",
    "age": 25,
    "job": "Data Analyst",
    "salary": 15000
}

print(employee["name"])
print(employee["job"])

employee["salary"] = 18000
employee["experience"] = 3

print(employee)

print(employee.keys())
print(employee.values())
print(employee.items())


# Data Analyst Example

customer = {
    "customer_id": 101,
    "name": "Ahmed",
    "sales": 75000,
    "segment": "Premium"
}

if customer["sales"] >= 50000:
    print("High Value Customer")