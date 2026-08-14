# 04 - OOP for Data/AI + Best Practices

## OOP in Data Analysis

OOP can organize reusable data-processing components.

```python
class DataCleaner:

    def clean(self, data):
        return [x for x in data if x is not None]
OOP in Data Engineering

A pipeline can be represented as objects.

class Pipeline:

    def extract(self):
        pass

    def transform(self):
        pass

    def load(self):
        pass
OOP in Machine Learning

Models can be represented as classes.

class Model:

    def train(self, data):
        pass

    def predict(self, data):
        pass
Best Practices
Single Responsibility

A class should have one clear responsibility.

Encapsulation

Keep internal implementation details protected.

Composition

Prefer combining objects when inheritance is unnecessary.

Reusability

Build reusable classes and methods.

Type Hints
def process(data: list) -> list:
    ...
Docstrings

Document classes and important methods.

Avoid Huge Classes

Split unrelated responsibilities into separate classes.

OOP Architecture Example
DataSource
    ↓
DataCleaner
    ↓
DataTransformer
    ↓
Model
    ↓
PredictionService

This pattern can be used in:

ETL
Data Analysis
Machine Learning
AI applications
APIs
Automation