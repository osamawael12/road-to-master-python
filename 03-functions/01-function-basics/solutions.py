# Exercise 01

def greet():
    print("Welcome to Python")


greet()


# Exercise 02

def greet_user(name):
    print(f"Hello {name}")


greet_user("Osama")


# Exercise 03

def calculate_sum(a, b):
    return a + b


print(calculate_sum(10, 20))


# Exercise 04

def calculate_profit(sales, cost):
    return sales - cost


print(calculate_profit(500000, 320000))


# Exercise 05

def calculate_margin(sales, cost):
    profit = sales - cost
    return profit / sales * 100


print(calculate_margin(500000, 320000))