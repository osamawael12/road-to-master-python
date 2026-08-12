# Exercise 01
for number in range(1, 11):
    if number == 7:
        break
    print(number)


# Exercise 02
for number in range(1, 11):
    if number == 5:
        continue
    print(number)


# Exercise 03
sales = [10000, -5000, 25000, -1000, 30000]

for sale in sales:
    if sale < 0:
        continue
    print(sale)


# Exercise 04
sales = [10000, 25000, 45000, 60000, 70000]

for sale in sales:
    if sale >= 50000:
        print("First Sale:", sale)
        break


# Exercise 05
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)