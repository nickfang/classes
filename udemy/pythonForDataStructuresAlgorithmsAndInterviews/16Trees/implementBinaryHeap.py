# binary heap implemented with a list
import random

class BinaryHeap(object):
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	# perculate an inserted item up until it is in the right position
	def percUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				temp = self.heapList[i//2]
				self.heapList[i//2] = self.heapList[i]
				self.heapList[i] = temp
			i = i // 2

	# insert an item at the end of the list and then perculate it up the tree until it is greater than both it's children
	def insert(self, val):
		self.heapList.append(val)
		self.currentSize += 1
		self.percUp(self.currentSize)

	# return the smallest child
	# if there is only one child return that index otherwise figure out the smaller one and return the index
	def minChild(self, i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

	# move an item down the tree if it is larger than it's smallest child
	def percDown(self, i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				temp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = temp
			i = mc

	# remove the smallest value.  The top of the tree (index 1) will always be the smallest.
	# then move last item in the list to the first index
	# perculate the item down until it is in the correct location
	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval

	# take an array of value and create a heap by starting half way through the list and perculate down as you move lower in the list
	def buildHeap(self, heapList):
		i = len(heapList) // 2
		self.currentSize = len(heapList)
		self.heapList = [0] + heapList[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1


A = []
for x in range(10):
	A.append(random.randint(0,100))
binHeap = BinaryHeap()
binHeap.buildHeap(A)
print(binHeap.heapList)
