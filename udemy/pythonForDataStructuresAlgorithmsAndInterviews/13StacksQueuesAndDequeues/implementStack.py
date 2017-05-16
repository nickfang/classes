"""
Check if its empty
Push a new item
Pop an item
Peek at the top item
Return size
"""

class Stack(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		if len(self.items) == 0:
			return None
		else:
			return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

stack = Stack()
print(stack.isEmpty())
stack.push("one")
stack.push("two")
stack.push("three")
print(stack.size())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.size())
print(stack.pop())
print(stack.peek())
print(stack.size())