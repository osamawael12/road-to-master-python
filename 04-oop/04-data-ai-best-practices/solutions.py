from dataclasses import dataclass


# Exercise 01

class DataCleaner:

    def clean(self, data: list) -> list:
        return [
            value for value in data
            if value is not None
        ]


# Exercise 02

class DataTransformer:

    def transform(self, data: list) -> list:
        return [
            value * 2
            for value in data
        ]


# Exercise 03

class Pipeline:

    def __init__(self, cleaner, transformer):
        self.cleaner = cleaner
        self.transformer = transformer

    def run(self, data):
        data = self.cleaner.clean(data)
        return self.transformer.transform(data)


pipeline = Pipeline(
    DataCleaner(),
    DataTransformer()
)

print(
    pipeline.run(
        [10, None, 20, 30]
    )
)


# Exercise 04

class Model:

    def train(self, data):
        print("Model trained")

    def predict(self, data):
        return [1 for _ in data]


model = Model()

model.train([10, 20, 30])

print(
    model.predict([100, 200])
)


# Exercise 05

@dataclass
class Prediction:

    customer_id: int
    probability: float
    label: str


prediction = Prediction(
    101,
    0.95,
    "High Risk"
)

print(prediction)


# Exercise 06

# Composition allows us to combine small,
# focused classes instead of creating large
# and complicated inheritance hierarchies.