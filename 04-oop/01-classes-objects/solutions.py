class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


product1 = Product("Laptop", 25000, 2)
product2 = Product("Mouse", 500, 5)

print(product1.total_value())
print(product2.total_value())


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_annual_salary(self):
        return self.salary * 12


employee = Employee("Osama", 20000)

print(employee.get_annual_salary())