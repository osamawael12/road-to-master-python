import csv
import json


# Exercise 01

with open("skills.txt", "w") as file:
    file.write("Python\n")
    file.write("SQL\n")
    file.write("Power BI\n")


# Exercise 02

with open("skills.txt", "r") as file:
    print(file.read())


# Exercise 03

sales = [
    ["name", "sales"],
    ["Ahmed", 50000],
    ["Ali", 75000],
    ["Omar", 30000]
]

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sales)


# Exercise 04

with open("sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


# Exercise 05

profile = {
    "name": "Ahmed",
    "age": 25,
    "skills": [
        "Python",
        "SQL",
        "Power BI"
    ]
}


# Exercise 06

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)


# Exercise 07

with open("profile.json", "r") as file:
    data = json.load(file)

print(data["skills"])