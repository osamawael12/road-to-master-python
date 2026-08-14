# 02 - Paths, OS & Data Handling

## pathlib

Use `pathlib` to work with files and directories.

```python
from pathlib import Path

path = Path("data/sales.csv")

print(path.exists())
print(path.name)
print(path.suffix)
Create Directory
folder = Path("data")
folder.mkdir(exist_ok=True)
List Files
for file in Path("data").iterdir():
    print(file)
OS Module
import os

print(os.getcwd())
Environment Variables
import os

api_key = os.getenv("API_KEY")

Never hard-code secrets.

Data Handling

A common workflow:

Raw Data
   ↓
Read
   ↓
Validate
   ↓
Clean
   ↓
Transform
   ↓
Save
Data / AI Connection

These concepts are essential for:

ETL
Data pipelines
Automation
APIs
Machine Learning
AI projects