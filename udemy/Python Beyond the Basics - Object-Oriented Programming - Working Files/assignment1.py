class MaxSizeList(object):
	def __init__(self, size):
		self.size = size
		self.values = []

	def push(self, value):
		self.values.append(value)
		if len(self.values) > self.size:
			self.values.pop(0)

	def get_list(self):
		return self.values