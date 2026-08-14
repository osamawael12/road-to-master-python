# Exercise 01

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)


countdown(5)


# Exercise 02

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


# Exercise 03

def recursive_sum(n):
    if n == 0:
        return 0

    return n + recursive_sum(n - 1)


print(recursive_sum(5))


# Exercise 04

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))


# Exercise 05

# Base Case:
# Stops the recursion.

# Recursive Case:
# Calls the function again with a smaller/simpler problem.