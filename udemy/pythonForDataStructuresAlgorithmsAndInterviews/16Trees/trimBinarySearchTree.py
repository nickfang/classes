# given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the new tree are between min and max inclusive.  The resulting tree should still be a valid binary search tree.

# didn't finish on my own
def trimBST(tree, minVal, maxVal):

	print(tree.left)
	print(tree.right)
	print(tree.val)

	if tree != None:
		trimBST(tree.left)
		# logic for trimming the tree
		if tree.val == minVal:
			tree.left = None
		if tree.val == maxVal:
			tree.right = None

		trimBST(tree.right)

# solution >>
def trimBST(tree, minVal, maxVal):
	if not tree:
		return

	tree.left = trimBST(tree.left, minVal, maxVal)
	tree.right = trimBST(tree.right, minVal, maxVal)

	if minVal <= tree.val <=maxVal:
		return tree

	if tree.val < minVal:
		return tree.right

	if tree.val > maxVal:
		return tree.left


# << solution