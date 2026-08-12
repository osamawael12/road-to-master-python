# Creating strings

name = "Osama"
message = 'Python for Data Analysis'

print(name)
print(message)


# Indexing

text = "Python"

print(text[0])
print(text[-1])


# Slicing

print(text[0:3])
print(text[2:])
print(text[:4])


# String methods

name = "  osama wael  "

print(name.upper())
print(name.lower())
print(name.strip())
print(name.title())
print(name.replace("osama", "ahmed"))


# Split and Join

data = "Python,SQL,Power BI"

skills = data.split(",")

print(skills)

print(" | ".join(skills))


# f-string

name = "Osama"
sales = 500000

print(f"{name} generated {sales} in sales.")


# Data Analyst Example

customer = "  OSAMA WAE L  "

customer = customer.strip().title()

print(customer)