# given a binary tree, check whether it's a binary search tree or not

# perform an inorder traverse and check if the result is in order

def traverseTree(node):
	if node != None:
		traverseTree(node.left)
		yield node.value
		traverseTree(node.right)

def solution()
	values = []
	for itr in traverseTree(node):
		values.append(itr)

	return values == sorted(values)
