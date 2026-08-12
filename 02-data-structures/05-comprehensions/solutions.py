numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)

odd_numbers = [x for x in numbers if x % 2 != 0]

print(odd_numbers)

sales = [10000, 25000, 50000, 75000, 100000]

high_sales = [sale for sale in sales if sale >= 50000]

print(high_sales)

squares_dict = {x: x ** 2 for x in numbers}

print(squares_dict)