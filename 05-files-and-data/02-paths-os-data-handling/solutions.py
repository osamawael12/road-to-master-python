from pathlib import Path
import os


# Exercise 01

print(Path.cwd())


# Exercise 02

datasets = Path("datasets")

datasets.mkdir(exist_ok=True)


# Exercise 03

sales_file = datasets / "sales.txt"


# Exercise 04

sales_file.write_text(
    "10000\n25000\n50000\n"
)


# Exercise 05

print(
    sales_file.read_text()
)


# Exercise 06

print(
    sales_file.exists()
)


# Exercise 07

for file in datasets.iterdir():
    print(file)


# Exercise 08

# API keys are secrets.
# Hard-coding them can expose credentials
# in GitHub repositories and source code.