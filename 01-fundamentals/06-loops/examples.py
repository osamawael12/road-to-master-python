# for loop

for i in range(5):
    print(i)


# Loop through values

sales = [1000, 2500, 3000, 4500]

for sale in sales:
    print(sale)


# Calculate total sales

total = 0

for sale in sales:
    total += sale

print("Total Sales:", total)


# while loop

counter = 1

while counter <= 5:
    print(counter)
    counter += 1


# Data Analyst Example

sales = [10000, 25000, 15000, 30000]

for sale in sales:
    if sale >= 20000:
        print("High Sale:", sale)