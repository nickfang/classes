import ctypes

class M(object):
	def public(self):
		print("Use Tab to see me!")
	def _private(self):
		# It's talking about tabbing to autocomplete in some development environments
		print("You won't be able to use Tab to see me!")

m = M()
m.public()
m._private()

class DynamicArray(object):
	def __init__(self):
		self.n = 0
		self.capacity = 1
		self.A = self.makeArray(self.capacity)

	def __len__(self):
		return self.n

	def __getitem__(self, k):
		if not 0 <= k < self.n:
			return IndexError('K is out of bounds!')
		return self.A[k]

	def append(self, element):
		if self.n == self.capacity:
			self._resize(2*self.capacity) # 2x if capacity isn't enough
		self.A[self.n] = element
		self.n += 1

	def _resize(self, new_capacity):
		B = self.makeArray(new_capacity)
		for k in range(self.n):
			B[k] = self.A[k]
		self.A = B
		self.capacity = new_capacity

	def makeArray(self, new_capacity):
		return(new_capacity * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print("Array length: ", len(arr))
arr.append(2)
print("Array length: ", len(arr))
