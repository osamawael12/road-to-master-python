# Exercise 01

stack = []

stack.append("Python")
stack.append("SQL")
stack.append("Power BI")

removed = stack.pop()

print("Removed:", removed)
print("Stack:", stack)


# Exercise 02

from collections import deque

queue = deque()

queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

processed = queue.popleft()

print("Processed:", processed)
print("Queue:", queue)


# Exercise 03

etl_queue = deque()

etl_queue.append("Extract")
etl_queue.append("Transform")
etl_queue.append("Load")

while etl_queue:
    step = etl_queue.popleft()
    print("Processing:", step)


# Exercise 04

# Stack → LIFO
# Queue → FIFO