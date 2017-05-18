# Given a binary tree of integers, print it in level order.  The output will contain space between the numbers in the same leve and a new line between different levels.

class Node:
	def __init__(self, val=None):
		self.left = None
		self.right = None
		self.val = val

def levelOrderPrint(tree):
	pass


# solution >>
# use a deque to keep track of the current level.
# After you get all elements on a level, add elements from the next level on the right side as you popleft() to remove the current level.
# need two variables to keep track of number of elements on current level and next level.  when no more elements on current level, make num next level num current level
import collections

def levelOrderPrint(tree):
	if not tree:
		return

	nodes = collections.deque([tree])

	currentCount = 1
	nextCount = 0
	while len(nodes) != 0:
		currentNode = nodes.popleft()
		currentCount -= 1

		print(currentNode.val, end=" ")

		if currentNode.left:
			nodes.append(currentNode.left)
			nextCount += 1

		if currentNode.right:
			nodes.append(currentNode.right)
			nextCount += 1
		if currentCount == 0:
			print()
			currentCount, nextCount = nextCount, currentCount

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

# nodes = collections.deque([root])
# print(nodes.pop().val)
# print(nodes.popleft().val)



levelOrderPrint(root)

# << solution
