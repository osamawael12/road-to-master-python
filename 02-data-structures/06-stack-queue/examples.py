
### `examples.py`

```python
# Stack

stack = []

stack.append("Load Data")
stack.append("Clean Data")
stack.append("Analyze Data")

print(stack)

last_task = stack.pop()

print("Completed:", last_task)
print("Remaining:", stack)


# Queue

from collections import deque

queue = deque()

queue.append("Customer 1")
queue.append("Customer 2")
queue.append("Customer 3")

print(queue)

first_customer = queue.popleft()

print("Processed:", first_customer)
print("Remaining:", queue)