# 01 - Files, CSV, JSON & TXT

## Text Files

Read:

```python
with open("data.txt", "r") as file:
    content = file.read()

Write:

with open("data.txt", "w") as file:
    file.write("Python")

Append:

with open("data.txt", "a") as file:
    file.write("\nSQL")
CSV
import csv

with open("sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
JSON
import json

with open("data.json") as file:
    data = json.load(file)

Write JSON:

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
Data Analysis Connection

Files are used for:

Dataset loading
ETL
Data preprocessing
API data
Configuration
Data pipelines