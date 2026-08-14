# Exercise 01

def calculate_sum(*numbers):
    return sum(numbers)


print(calculate_sum(10, 20, 30, 40))


# Exercise 02

def calculate_average(*numbers):
    return sum(numbers) / len(numbers)


print(calculate_average(10, 20, 30, 40))


# Exercise 03

def show_employee(**employee):
    for key, value in employee.items():
        print(f"{key}: {value}")


show_employee(
    name="Osama",
    department="Analytics",
    salary=15000
)


# Exercise 04

def report(*sales, **metadata):
    print("Total Sales:", sum(sales))
    print("Metadata:", metadata)


report(
    10000,
    20000,
    30000,
    department="Sales",
    year=2026
)


# Exercise 05

def employee_skills(name, *skills):
    print("Name:", name)

    for skill in skills:
        print("Skill:", skill)


employee_skills(
    "Osama",
    "Python",
    "SQL",
    "Power BI"
)