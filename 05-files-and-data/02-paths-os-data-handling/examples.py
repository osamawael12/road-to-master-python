
### `examples.py`

```python
from pathlib import Path
import os


# Current directory

print(Path.cwd())


# Create directory

data_folder = Path("data")

data_folder.mkdir(exist_ok=True)


# Create file

file_path = data_folder / "sales.txt"

file_path.write_text(
    "10000\n25000\n50000\n"
)


# Read file

content = file_path.read_text()

print(content)


# Check file

print(file_path.exists())
print(file_path.name)
print(file_path.suffix)


# List files

for file in data_folder.iterdir():
    print(file)


# Environment variable

api_key = os.getenv("API_KEY")

print(api_key)