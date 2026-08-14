# Exercise 01

def show_sales():
    sales = 500000
    print(sales)


show_sales()


# Exercise 02

company = "Data Analytics Inc."


def show_company():
    print(company)


show_company()


# Exercise 03

counter = 0


def increase_counter():
    global counter
    counter += 1


increase_counter()

print(counter)


# Exercise 04

def outer():
    value = 10

    def inner():
        nonlocal value
        value += 10

    inner()

    return value


print(outer())