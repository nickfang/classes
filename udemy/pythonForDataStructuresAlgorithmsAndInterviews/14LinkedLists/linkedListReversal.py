class Node(object):
	def __init__(self, value):
		self.value = value
		self.nextNode = None

def reverse(head):
	itr1 = head
	itr2 = None
	if itr1 == None or itr1.nextNode == None:
		return head
	while itr1:
		temp = itr1
		if itr1.nextNode is None:
			itr1.nextNode = itr2
			return itr1
		else:
			itr1 = itr1.nextNode
			temp.nextNode = itr2
			itr2 = temp

# solution >>
def reverse2(head):
	current = head
	previous = None
	nextNode = None
	while current:
		nextNode = current.nextNode
		current.nextNode = previous
		previous = current
		current = nextNode
	return previous
# << solution

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextNode = b
b.nextNode = c
c.nextNode = d

node = reverse2(a)
while node is not None:
	print(node.value)
	node = node.nextNode