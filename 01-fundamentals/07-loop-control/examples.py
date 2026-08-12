# break
for number in range(1, 11):
    if number == 6:
        break
    print(number)


# continue
for number in range(1, 11):
    if number == 5:
        continue
    print(number)


# pass
for number in range(5):
    if number == 2:
        pass
    print(number)


# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# Data Analyst Example
sales = [10000, 25000, -5000, 30000]

for sale in sales:
    if sale < 0:
        print("Invalid Sale:", sale)
        continue

    print("Valid Sale:", sale)