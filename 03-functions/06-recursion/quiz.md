# Quiz 06 - Recursion

## Q1
What is recursion?

## Q2
What are the two essential parts of recursion?

## Q3
Why is the Base Case important?

## Q4
What is the output?

```python
def test(n):
    if n == 0:
        return

    print(n)
    test(n - 1)

test(3)
Q5

What is:

factorial(5)
Q6

What happens if a recursive function has no Base Case?

Q7

Give one Data/AI use case for recursion.


### Answers

```text
Q1 → A function calling itself
Q2 → Base Case + Recursive Case
Q3 → It stops the recursion
Q4 →
3
2
1

Q5 → 120
Q6 → Infinite recursion / RecursionError
Q7 → Tree/Graph traversal, searching, divide and conquer