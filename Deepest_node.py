# Problem : Given the root to a binary tree, return the deepest node.

def deepest(node):
	if not node.left and not node.right: # if it's a leaf node
		return(node, 1) # return a leaf node's depth

	if not node.left: # if no left child then ddepest is in the right subtree
		return increment_depth(deepest(node.right))

	elif not node.right: # if no right child then ddepest is in the left subtree
		return increment_depth(deepest(node.left))

	# else go down both subtrees 	
	return increment_depth(max(deepest(node.left), deepest(node.right), key = lambda x: x[1]))

def increment_depth(node_depth_tuple):
	node, depth = node_depth_tuple
	return (node, depth+1)



class Node:
	def __init__(self, data = 5, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

root = Node()
root.left = Node()
root.left.right = Node(data = 10)

print(deepest(root))

# Output: (<__main__.Node object at 0x0000007B674E77B8>, 3)
# Correct




