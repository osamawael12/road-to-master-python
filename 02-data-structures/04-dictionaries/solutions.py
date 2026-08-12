employee = {
    "name": "Ahmed",
    "age": 28,
    "salary": 18000
}

print(employee["name"])
print(employee["salary"])

employee["department"] = "Analytics"

employee["salary"] = 20000

print(employee.get("department"))

for key, value in employee.items():
    print(key, ":", value)