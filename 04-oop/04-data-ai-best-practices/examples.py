
### `examples.py`

```python
from dataclasses import dataclass


class DataCleaner:

    def clean(self, data: list) -> list:
        return [
            value for value in data
            if value is not None
        ]


class DataTransformer:

    def transform(self, data: list) -> list:
        return [
            value * 1.10
            for value in data
        ]


class Pipeline:

    def __init__(self, cleaner, transformer):
        self.cleaner = cleaner
        self.transformer = transformer

    def run(self, data):
        data = self.cleaner.clean(data)
        data = self.transformer.transform(data)

        return data


cleaner = DataCleaner()
transformer = DataTransformer()

pipeline = Pipeline(
    cleaner,
    transformer
)

data = [100, None, 200, 300]

print(pipeline.run(data))


# ML-style example

class Model:

    def train(self, data):
        print(f"Training on {len(data)} records")

    def predict(self, data):
        return [1 for _ in data]


model = Model()

model.train([10, 20, 30])

print(model.predict([100, 200, 300]))


# Dataclass for structured data

@dataclass
class Prediction:

    customer_id: int
    probability: float
    label: str


prediction = Prediction(
    customer_id=101,
    probability=0.92,
    label="High Risk"
)

print(prediction)