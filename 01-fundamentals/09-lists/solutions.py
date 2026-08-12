
### `solutions.py`

```python
# Exercise 01
sales = [10000, 25000, 15000, 30000, 45000]

print("First:", sales[0])
print("Last:", sales[-1])
print("Total:", sum(sales))
print("Maximum:", max(sales))
print("Minimum:", min(sales))


# Exercise 02
sales.append(50000)

print(sales)


# Exercise 03
sales.remove(15000)

print(sales)


# Exercise 04
sales.sort()

print(sales)


# Exercise 05
count = 0

for sale in sales:
    if sale >= 30000:
        count += 1

print("Count:", count)