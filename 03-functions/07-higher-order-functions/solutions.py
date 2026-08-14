# Exercise 01

def apply_function(func, value):
    return func(value)


# Exercise 02

def double(x):
    return x * 2


# Exercise 03

print(
    apply_function(double, 10)
)


# Exercise 04

def multiplier(factor):

    def multiply(value):
        return value * factor

    return multiply


triple = multiplier(3)

print(triple(10))


# Exercise 05

def create_tax(rate):

    def calculate_tax(price):
        return price + price * rate

    return calculate_tax


tax_15 = create_tax(0.15)

print(tax_15(1000))