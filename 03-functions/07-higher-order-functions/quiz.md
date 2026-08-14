# Quiz 07 - Higher-Order Functions & Closures

## Q1
What is a Higher-Order Function?

## Q2
Can a function be passed as an argument?

A. Yes
B. No

## Q3
Can a function return another function?

A. Yes
B. No

## Q4
What is a Closure?

## Q5
What is the output?

```python
def multiplier(factor):

    def multiply(value):
        return value * factor

    return multiply

double = multiplier(2)

print(double(5))
Q6

Why are Higher-Order Functions useful?

Q7

Give one Data Analysis use case.

Q8

What variable does the Closure remember?