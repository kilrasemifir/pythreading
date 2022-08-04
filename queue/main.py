from queue import Queue
from collections import deque

# FIFO queue
q = Queue()

q.put(1)
q.put(2)
print([item for item in q.queue])
print(q.get())
print(q.get())

stack = deque()

stack.append("a")
stack.append("b")
print(stack)
print(stack.pop())
print(stack.pop())
