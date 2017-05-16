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
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

s = Stack()
# True
print(s.isEmpty())
s.push(1)
s.push("two")
# "two"
print(s.peek())
s.push(True)
#3
print(s.size())
#False
print(s.isEmpty())
#True
print(s.pop())
#"two"
print(s.pop())
# 1
print(s.pop())
