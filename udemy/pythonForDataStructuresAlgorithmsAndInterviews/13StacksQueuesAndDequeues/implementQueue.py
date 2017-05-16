"""
Check if Queue is empty
enqueue
dequeue
return the size of the queue
"""

class Queue(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size())
q.enqueue(4)
q.enqueue(5)
print(q.size())
print(q.dequeue())
print(q.isEmpty())
print(q.dequeue())
q.enqueue(6)
q.enqueue(7)
print(q.size())
q.enqueue(8)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())