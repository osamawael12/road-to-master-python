
### `examples.py`

```python
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

sales = [10000, 50000, 25000, 80000]

high_sales = [sale for sale in sales if sale >= 50000]

print(high_sales)

sales_map = {sale: sale * 2 for sale in sales}

print(sales_map)