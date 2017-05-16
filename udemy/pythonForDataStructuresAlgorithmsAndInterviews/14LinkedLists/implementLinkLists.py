class SLLNode(object):
	def __init__(self, value):
		self.value = value
		self.nextNode = None

class DLLNode(object):
	def __init__(self, value):
		self.value = value
		self.nextNode = None
		self.prevNode = None