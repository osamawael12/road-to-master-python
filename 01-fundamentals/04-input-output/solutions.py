# Exercise 01
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Welcome {name}, you are {age} years old.")


# Exercise 02
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Multiplication:", num1 * num2)


# Exercise 03
sales = float(input("Enter sales: "))
cost = float(input("Enter cost: "))

profit = sales - cost
profit_margin = profit / sales * 100

print("Profit:", profit)
print("Profit Margin:", profit_margin)


# Exercise 04
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount (%): "))

gross_sales = price * quantity
discount_amount = gross_sales * discount / 100
net_sales = gross_sales - discount_amount

print("Gross Sales:", gross_sales)
print("Discount:", discount_amount)
print("Net Sales:", net_sales)