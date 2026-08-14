
### `examples.py`

```python
import csv
import json


# =========================
# TXT
# =========================

with open("example.txt", "w") as file:
    file.write("Python\n")
    file.write("Data Analysis\n")


with open("example.txt", "r") as file:
    print(file.read())


# =========================
# CSV
# =========================

sales = [
    ["customer", "sales"],
    ["Ahmed", 50000],
    ["Ali", 75000],
    ["Omar", 30000]
]

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sales)


with open("sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


# =========================
# JSON
# =========================

data = {
    "name": "Ahmed",
    "role": "Data Analyst",
    "skills": [
        "Python",
        "SQL",
        "Power BI"
    ]
}

with open("profile.json", "w") as file:
    json.dump(data, file, indent=4)


with open("profile.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)