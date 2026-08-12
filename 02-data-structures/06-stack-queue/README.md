# 06 - Stack & Queue

## Stack

Stack follows LIFO:

Last In, First Out.

Python Lists can implement a Stack.

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

item = stack.pop()

print(item)

Output:

C
Queue

Queue follows FIFO:

First In, First Out.

Use collections.deque.

from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

item = queue.popleft()

print(item)

Output:

A
Data Analysis / AI Connection

Stacks and Queues are useful in:

Task processing
ETL pipelines
Job scheduling
BFS algorithms
Data processing systems
AI search algorithms