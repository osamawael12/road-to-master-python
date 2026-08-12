sales = [10000, 25000, 15000, 30000]

print(sales)
print(sales[0])
print(sales[-1])
print(sales[1:3])

sales.append(40000)
sales.insert(1, 12000)

sales.remove(15000)

print(sales)

sales.sort()
print(sales)

sales.reverse()
print(sales)

print(len(sales))
print(sum(sales))
print(max(sales))
print(min(sales))