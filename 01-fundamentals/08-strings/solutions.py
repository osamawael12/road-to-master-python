# Exercise 01
text = "Python Data Analysis"

print(text[0])
print(text[-1])
print(text[:6])


# Exercise 02
name = "  osama wael  "

clean_name = name.strip().title()

print(clean_name)


# Exercise 03
email = "osama@example.com"

username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)


# Exercise 04
skills = "Python,SQL,Power BI,Excel"

skills_list = skills.split(",")

print(skills_list)


# Exercise 05
product = "laptop computer"

print(product.title())


# Exercise 06
name = "Osama"
sales = 250000

print(f"{name} generated {sales} in sales.")