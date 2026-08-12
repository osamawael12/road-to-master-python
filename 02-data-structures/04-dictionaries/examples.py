
### `examples.py`

```python
customer = {
    "id": 101,
    "name": "Ahmed",
    "sales": 75000
}

print(customer["name"])

customer["sales"] = 90000
customer["segment"] = "VIP"

print(customer)

print(customer.keys())
print(customer.values())
print(customer.items())

print(customer.get("name"))

customer.pop("segment")

print(customer)