class Node:
	def __init__(self, value):
		self.value = value
		self.nextNode = None

def nthToLastNode(num, node):
	itr = node
	stack = []
	while itr:
		if len(stack) == num:
			stack.pop(0)
		stack.append(itr)
		itr = itr.nextNode
	return stack[0]

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e
e.nextNode = f

# this would return the node d with a value of 4, because it's the 2nd to last node.
targetNode = nthToLastNode(2,a)

# 4
print(targetNode.value)

# solution >>
def nthToLastNode2(n, head):
	leftPointer = head
	rightPointer = head

	for i in range(n-1):
		if not rightPointer.nextNode:
			raise LookupError("Error: n is larger than the linked list")

		rightPointer = rightPointer.nextNode

	while rightPointer.nextNode:
		leftPointer = leftPointer.nextNode
		rightPointer = rightPointer.nextNode
	return leftPointer
# << solution

"""
Run This Cell To Test Your Solution Against A Test Case
Please Note This Is Just One Case
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e
e.nextNode = f

####

class TestNLast(object):
	def test(self,sol):
		assert_equal(sol(2,a),e)
		print("All Test Cases Passed")

# Run Tests
t = TestNLast()
t.test(nthToLastNode)