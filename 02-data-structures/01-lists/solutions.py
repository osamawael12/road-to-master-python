# Exercise 01
sales = [10000, 25000, 15000, 30000, 45000]

print("First:", sales[0])
print("Last:", sales[-1])
print("Slice:", sales[1:4])


# Exercise 02
sales[2] = 20000

print(sales)


# Exercise 03
sales.append(50000)
sales.remove(10000)
sales.sort()

print(sales)


# Exercise 04
total = sum(sales)
average = total / len(sales)
maximum = max(sales)
minimum = min(sales)

print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)


# Exercise 05
sales = [10000, 25000, 5000, 45000, 30000]

high_sales = [sale for sale in sales if sale >= 20000]

print(high_sales)


# Exercise 06
employees = [
    ["Ahmed", 15000],
    ["Mohamed", 18000],
    ["Ali", 22000]
]

print(employees[2][1])