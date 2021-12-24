# create a function to visualize a binary tree

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def displayBinaryTree(node, space='\t', level=0):
    # if node is empty
    if node is None:
        print(space*level+ '∅')
        return
    
    # if the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return 
    
    displayBinaryTree(node.right, space, level+1)
    print(space*level + str(node.key))
    displayBinaryTree(node.left, space, level+1)