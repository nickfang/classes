def preOrder(tree):
	if tree != None:
		print(tree.getRootVal())
		preOrder(tree.getLeftChild())
		preOrder(tree.getRightChild())

def postOrder(tree)
	if tree != None:
		preOrder(tree.getLeftChild())
		preOrder(tree.getRightChild())
		print(tree.getRootVal())

def inOrder(tree):
	if tree != None:
		preOrder(tree.getLeftChild())
		print(tree.getRootVal())
		preOrder(tree.getRightChild())
