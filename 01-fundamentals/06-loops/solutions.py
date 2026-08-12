# Exercise 01
for i in range(1, 11):
    print(i)


# Exercise 02
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Sum:", total)


# Exercise 03
sales = [12000, 45000, 23000, 67000, 34000]

maximum = sales[0]

for sale in sales:
    if sale > maximum:
        maximum = sale

print("Maximum:", maximum)


# Exercise 04
sales = [10000, 35000, 45000, 12000, 50000, 20000]

count = 0

for sale in sales:
    if sale >= 30000:
        count += 1

print("Count:", count)


# Exercise 05
for number in range(1, 21):
    if number % 2 == 0:
        print(number)


# Exercise 06
number = 10

while number >= 1:
    print(number)
    number -= 1