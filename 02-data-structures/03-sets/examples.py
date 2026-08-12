
### `examples.py`

```python
skills = {"Python", "SQL", "Python", "Power BI"}

print(skills)

skills.add("Excel")
skills.remove("SQL")

print(skills)

set_a = {"Python", "SQL", "Excel"}
set_b = {"Python", "Power BI", "Excel"}

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))