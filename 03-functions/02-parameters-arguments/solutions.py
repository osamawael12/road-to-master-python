# Exercise 01

def calculate_total(price, quantity):
    return price * quantity


print(calculate_total(1000, 5))


# Exercise 02

def calculate_discount(price, quantity, discount):
    gross_sales = price * quantity
    discount_amount = gross_sales * discount / 100

    return gross_sales - discount_amount


print(calculate_discount(1000, 10, 20))


# Exercise 03

def greet(name="User"):
    print(f"Hello {name}")


greet()
greet("Osama")


# Exercise 04

def employee_info(name, department, salary):
    return f"{name} - {department} - {salary}"


print(
    employee_info(
        name="Osama",
        department="Analytics",
        salary=15000
    )
)


# Exercise 05

def calculate_margin(sales, cost):
    profit = sales - cost
    return profit / sales * 100


print(
    calculate_margin(
        sales=500000,
        cost=320000
    )
)