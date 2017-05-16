class DoublyLinkListNode(object):
	def __init__(self, value):
		self.value = value
		self.nextNode = None
		self.prevNode = None

a = DoublyLinkListNode(1)
b = DoublyLinkListNode(2)
c = DoublyLinkListNode(3)

a.nextNode = b
b.prevNode = a
b.nextNode = c
c.prevNode = b

