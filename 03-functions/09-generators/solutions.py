# Exercise 01

def numbers():
    for i in range(1, 6):
        yield i


print(list(numbers()))


# Exercise 02

def count_down(n):
    while n >= 1:
        yield n
        n -= 1


print(list(count_down(5)))


# Exercise 03

def even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            yield i


print(list(even_numbers()))


# Exercise 04

squares = (x ** 2 for x in range(1, 11))

print(list(squares))


# Exercise 05

# Generators process values one at a time,
# so they consume less memory.