class Node(object):
	def __init__(self, value):
		self.value = value
		self.nextNode = None

def cycleCheck(node):
	itr1 = node

	if (itr1 == None or itr1.nextNode == None):
		return False

	while itr1 is not None:
		itr2 = node
		while itr2 is not itr1:
			if itr2 == itr1.nextNode:
				return True
			else:
				itr2 = itr2.nextNode
		itr1 = itr1.nextNode
	return False


# solution >>
def cycleCheck2(node):
	marker1 = node
	marker2 = node
	while marker2 != None and marker2.nextNode != None:
		marker1 = marker1.nextNode
		marker2 = marker2.nextNode.nextNode

		if marker2 == marker1:
			return True
	return False

# << solution

"""
Run This Cell to Test Your Solution
"""
from nose.tools import assert_equal

# Create Cycle List
a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c
c.nextNode = a # cycle here

# Create Non Cycle List
x = Node(1)
y = Node(2)
z = Node(3)

x.nextNode = y
y.nextNode = z

##############
class TestCycleCheck(object):
	def test(self, sol):
		assert_equal(sol(a), True)
		assert_equal(sol(x), False)
		print("All Test Cases Passed")

# Run Test
t = TestCycleCheck()
t.test(cycleCheck2)