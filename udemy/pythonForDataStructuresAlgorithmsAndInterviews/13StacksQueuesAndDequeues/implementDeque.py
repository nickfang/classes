"""
check if it's empty
add to both front and rear
remove from front and rear
check size
"""
class Deque(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

d = Deque()
print(d.size())
print(d.isEmpty())
d.addFront("front1")
d.addFront("front2")
print(d.isEmpty())
print(d.removeFront())
d.addRear("rear1")
d.addRear("rear2")
d.addRear("rear3")
print(d.size())
print(d.removeRear())
print(d.removeFront())
print(d.size())
print(d.removeRear())
print(d.removeFront())
print(d.isEmpty())