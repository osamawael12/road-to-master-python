
### `examples.py`

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Iterator with for loop

iterator = iter(numbers)

for number in iterator:
    print(number)


# String Iterator

text = "Python"

iterator = iter(text)

print(next(iterator))
print(next(iterator))


# Generator is an Iterator

def numbers_generator():
    yield 100
    yield 200
    yield 300


generator = numbers_generator()

print(next(generator))
print(next(generator))
print(next(generator))