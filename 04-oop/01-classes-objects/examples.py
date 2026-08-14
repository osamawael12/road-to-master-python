
### `examples.py`

class Customer:

    def __init__(self, name, sales):
        self.name = name
        self.sales = sales

    def get_sales(self):
        return self.sales

    def is_vip(self):
        return self.sales >= 50000


customer1 = Customer("Ahmed", 75000)
customer2 = Customer("Ali", 30000)

print(customer1.name)
print(customer1.get_sales())
print(customer1.is_vip())

print(customer2.name)
print(customer2.is_vip())